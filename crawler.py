# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import argparse
import json
import sys
from io import open
from datetime import datetime
from multiprocessing.pool import ThreadPool
from time import sleep

import math

from inscrawler import InsCrawler
from inscrawler.settings import override_settings
from inscrawler.settings import prepare_override_settings

from inscrawler.persist import Persist
import dateutil.parser


def usage():
    return """
        python crawler.py posts -u cal_foodie -n 100 -o ./output
        python crawler.py posts_full -u cal_foodie -n 100 -o ./output
        python crawler.py profile -u cal_foodie -o ./output
        python crawler.py profile_script -u cal_foodie -o ./output
        python crawler.py hashtag -t taiwan -o ./output

        The default number for fetching posts via hashtag is 100.
    """


def get_posts_by_user(username, number, detail, debug):
    ins_crawler = InsCrawler(has_screen=debug)
    ins_crawler.login()
    return ins_crawler.get_user_posts(username, number, detail)


def get_profile(username, debug=False, follow_list_enabled=False):
    ins_crawler = InsCrawler(has_screen=debug)
    ins_crawler.login()
    return ins_crawler.get_user_profile(username, None, follow_list_enabled)


def get_profile_from_script(username):
    ins_cralwer = InsCrawler()
    return ins_cralwer.get_user_profile_from_script_shared_data(username)


def get_posts_by_hashtag(tag, number, debug):
    ins_crawler = InsCrawler(has_screen=debug)
    return ins_crawler.get_latest_posts_by_tag(tag, number)


def get_user_profile_worker(ins_crawler, tab, missing_profile_usernames, debug):
    print('Running thread for ', missing_profile_usernames)

    for missed_username in missing_profile_usernames:
        missed_profile = ins_crawler.get_user_profile(
            missed_username, tab, False)
        missed_profile['username'] = missed_username
        print('Persisting profile of ', missed_username, '...')
        persist.persistProfile(missed_profile)
        print('Persisting done for ', missed_username, '.')
    ins_crawler.browser.switch_to_tab(tab)
    ins_crawler.browser.release_lock()
    ins_crawler.browser.close_current_tab()
    print('End!')


def arg_required(args, fields=[]):
    for field in fields:
        if not getattr(args, field):
            parser.print_help()
            sys.exit()


def output(data, filepath):
    out = json.dumps(data, ensure_ascii=False)
    if filepath:
        with open(filepath, "w", encoding="utf8") as f:
            f.write(out)
    else:
        print(out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Instagram Crawler", usage=usage())
    parser.add_argument(
        "mode", help="options: [posts, posts_full, profile, profile_script, hashtag]"
    )
    parser.add_argument("-n", "--number", type=int,
                        help="number of returned posts")
    parser.add_argument("-u", "--username", help="instagram's username")
    parser.add_argument("-t", "--tag", help="instagram's tag name")
    parser.add_argument("-o", "--output", help="output file name(json format)")
    parser.add_argument("--debug", action="store_true")

    prepare_override_settings(parser)

    args = parser.parse_args()

    override_settings(args)

    if args.mode in ["posts", "posts_full"]:
        arg_required("username")
        posts = get_posts_by_user(
            args.username, args.number, args.mode == "posts_full", args.debug
        )
        persist = Persist()
        id_profile = persist.getUserIdByUsername(args.username)

        if id_profile is None:
            raise Exception('The profile of specified username does not exist')

        for post in posts:
            post['id_profile'] = id_profile
            persist.persistPost(post)

            for comment in post['comments'] if 'comments' in post.keys() else []:
                author = comment['author']
                id_profile = persist.getUserIdByUsername(author)
                if id_profile is None:
                    profile = get_profile(author)
                    profile['username'] = author
                    persist.persistProfile(profile)
                    id_profile = persist.getUserIdByUsername(author)

                id_post = persist.getPostIdByUrl(post['key'])

                comment['id_author'] = id_profile
                comment['id_post'] = id_post

                if id_post is None:
                    raise Exception('The specified post does not exist')

                id_comment = persist.getNextSequenceId('comment_id_seq')
                persist.persistComment(comment, None, id_comment)

                for liker in comment['likers'] if 'likers' in comment.keys() else []:
                    id_profile = persist.getUserIdByUsername(liker)
                    if id_profile is None:
                        profile = get_profile(liker)
                        profile['username'] = liker
                        persist.persistProfile(profile)
                        id_profile = persist.getUserIdByUsername(liker)

                    persist.persistLikeOnComment(id_profile, id_comment)

            for liker in post['likers'] if 'likers' in post.keys() else []:
                id_profile = persist.getUserIdByUsername(liker)
                if id_profile is None:
                    profile = get_profile(liker)
                    profile['username'] = liker
                    persist.persistProfile(profile)
                    id_profile = persist.getUserIdByUsername(liker)

                id_post = persist.getPostIdByUrl(post['key'])

                if id_post is None:
                    raise Exception('The specified post does not exist')

                persist.persistLikeOnPost(id_profile, id_post)

        output(posts, args.output,)

    elif args.mode == "profile":
        n_threads = 2
        thread_pool = ThreadPool(n_threads)

        arg_required("username")

        ins_crawler = InsCrawler(has_screen=args.debug)
        ins_crawler.login()

        profile = ins_crawler.get_user_profile(args.username, None, True)
        profile['capture_time'] = int(datetime.now().timestamp())

        output(profile, args.output)
        persist = Persist()
        profile["username"] = args.username
        persist.persistProfile(profile)

        # Check for missing followers in database and persist them
        missing_profile_usernames = list(
            persist.getMissingProfiles(profile['followers']))
        chunk_size = math.ceil(len(missing_profile_usernames) / n_threads)

        tab_handles = list()
        for i in range(n_threads):
            current_tab = ins_crawler.browser.driver.current_window_handle
            tab_handles.append(ins_crawler.browser.create_tab())

        for i in range(n_threads):
            thread_pool.apply_async(get_user_profile_worker, (ins_crawler, tab_handles[i],
                                                              missing_profile_usernames[i * chunk_size: (i + 1) * chunk_size], args.debug))

        thread_pool.close()
        thread_pool.join()

        # persist.persistFollowing(profile)

    elif args.mode == "profile_script":
        arg_required("username")
        output(get_profile_from_script(args.username), args.output)
    elif args.mode == "hashtag":
        arg_required("tag")
        output(
            get_posts_by_hashtag(
                args.tag, args.number or 100, args.debug), args.output
        )
    else:
        usage()
