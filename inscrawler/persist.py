from .database.postgres import connect
from datetime import datetime
import dateutil.parser


class Persist():
    def __init__(self):
        super().__init__()
        self.db = connect()
        if self.db is None:
            return
        self.createTables()

    def createTables(self):
        commands = [
            """
            CREATE TABLE IF NOT EXISTS profile
            (
                id SERIAL NOT NULL,
                username TEXT NOT NULL UNIQUE,
                name TEXT,
                description TEXT,
                n_followers INTEGER,
                n_following INTEGER,
                n_posts INTEGER,
                photo_url TEXT,
                last_visit BIGINT,
                created_at BIGINT,
                deleted BOOLEAN,
                PRIMARY KEY (id)
            );
            CREATE TABLE IF NOT EXISTS post
            (
                id SERIAL NOT NULL,
                id_profile INTEGER REFERENCES profile(id),
                url TEXT,
                url_imgs TEXT,
                post_date BIGINT,
                caption TEXT,
                last_visit BIGINT,
                deleted BOOLEAN,
                PRIMARY KEY (id)
            );
            CREATE TABLE IF NOT EXISTS comment
            (
                id SERIAL NOT NULL,
                id_post INTEGER REFERENCES post(id),
                id_author INTEGER REFERENCES profile(id),
                comment TEXT,
                last_visit BIGINT,
                deleted BOOLEAN,
                PRIMARY KEY (id)
            );
            CREATE TABLE IF NOT EXISTS like_on_comment
            (
                id_profile INTEGER REFERENCES profile(id),
                id_comment INTEGER REFERENCES comment(id),
                created_at BIGINT,
                last_visit BIGINT,
                deleted BOOLEAN,
                PRIMARY KEY (id_profile, id_comment)
            );
            CREATE TABLE IF NOT EXISTS like_on_post
            (
                id_profile INTEGER REFERENCES profile(id),
                id_post INTEGER REFERENCES post(id),
                last_visit BIGINT,
                created_at BIGINT,
                deleted BOOLEAN,
                PRIMARY KEY (id_profile,id_post)
            );
            CREATE TABLE IF NOT EXISTS following
            (
                id_followed INTEGER REFERENCES profile(id),
                id_follower INTEGER REFERENCES profile(id),
                last_visit BIGINT,
                created_at BIGINT,
                deleted BOOLEAN,
                PRIMARY KEY (id_followed,id_follower)
            );
            """
        ]
        cur = self.db.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        self.db.commit()


    def getMissingProfiles(self, profile_list):
        """Return list of non-persisted profiles"""
        missing_profiles = []
        for profile in profile_list if profile_list is not None else []:
            if self.getUserIdByUsername(profile) is None:
                missing_profiles.append(profile)

        return missing_profiles

    def getUserIdByUsername(self, username):
        if self.db is None:
            return

        sql = """
            SELECT id FROM profile WHERE username = '%s';
        """ % (username)

        cur = self.db.cursor()
        cur.execute(sql)
        ids_profile = cur.fetchall()
        if len(ids_profile) > 0:
            id_profile = ids_profile[0][0]
        else:
            id_profile = None

        cur.close()

        return id_profile

    def getNextSequenceId(self, sequence):
        if self.db is None:
            return

        sql = """
            SELECT nextval('%s')
        """ %(sequence)

        cur = self.db.cursor()
        cur.execute(sql)
        id = cur.fetchone()[0]
        cur.close()
        return id

    def getPostIdByUrl(self, url):
        if self.db is None:
            return

        sql = """
            SELECT id FROM post WHERE url = '%s';
        """ % (url)

        cur = self.db.cursor()
        cur.execute(sql)
        ids_post = cur.fetchall()
        if len(ids_post) > 0:
            id_post = ids_post[0][0]
        else:
            id_post = None

        cur.close()

        return id_post

    def persistFollowing(self, profile):
        print('Persisting follow relation...')
        if self.db is None:
            return

        id_followed = self.getUserIdByUsername(profile['username'])
        for user_following in profile['followers']:
            id_follower = self.getUserIdByUsername(user_following)

            sql = """
                INSERT INTO following(id_followed, id_follower, last_visit, created_at, deleted)
                VALUES(%s, %s, %s, %s, %s);
            """
            cur = self.db.cursor()
            cur.execute(sql, (id_followed, id_follower, int(datetime.now().timestamp()), int(datetime.now().timestamp())), False)

        self.db.commit()
        print('Done!')
        cur.close()

    def persistProfile(self, profile):
        if self.db is None:
            return
        sql = """
            INSERT INTO profile(username, name, description, n_followers, n_following, n_posts, photo_url, last_visit, created_at)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cur = self.db.cursor()
        cur.execute(sql, (profile["username"], profile["name"], profile["desc"], profile["follower_num"], profile["following_num"],
                          profile["post_num"], profile["photo_url"], int(datetime.now().timestamp()), int(datetime.now().timestamp())))
        self.db.commit()
        cur.close()

    def persistPost(self, post):
        if self.db is None:
            return
        sql = """
            INSERT INTO post(id_profile, url, url_imgs, post_date, caption, last_visit, deleted)
            VALUES(%s, %s, %s, %s, %s, %s, %s);
        """
        cur = self.db.cursor()

        cur.execute(sql, (post['id_profile'], post['key'], ",".join(post['img_urls']), int(dateutil.parser.parse(post['datetime']).timestamp()),
                          post['caption'], int(datetime.now().timestamp()), False))
        self.db.commit()
        cur.close()

    def persistComment(self, comment, id_comment_reply, id=None):
        if self.db is None:
            return
        cur = self.db.cursor()
        if id is None:
            sql = """
                INSERT INTO comment(id_post, id_author, comment, last_visit, deleted)
                VALUES(%s, %s, %s, %s, %s);
            """
            cur.execute(sql, (comment['id_post'], comment['id_author'], comment['comment'], int(
            datetime.now().timestamp()), False))
        else:
            sql = """
                INSERT INTO comment(id, id_post, id_author, comment, last_visit, deleted)
                VALUES(%s, %s, %s, %s, %s, %s);
            """
            cur.execute(sql, (id, comment['id_post'], comment['id_author'], comment['comment'], int(
            datetime.now().timestamp()), False))

        self.db.commit()
        cur.close()

    def persistLikeOnComment(self, id_profile, id_comment):
        if self.db is None:
            return
        sql = """
            INSERT INTO like_on_comment(id_profile, id_comment, created_at, last_visit, deleted)
            VALUES(%s, %s, %s, %s, %s);
        """
        cur = self.db.cursor()
        cur.execute(sql, (id_profile, id_comment, int(datetime.now().timestamp()), int(datetime.now().timestamp()), False))
        self.db.commit()
        cur.close()

    def persistLikeOnPost(self, id_profile, id_post):
        if self.db is None:
            return
        sql = """
            INSERT INTO like_on_post(id_profile, id_post, created_at, last_visit, deleted)
            VALUES(%s, %s, %s, %s, %s);
        """
        cur = self.db.cursor()
        cur.execute(sql, (id_profile, id_post, int(
            datetime.now().timestamp()), int(datetime.now().timestamp()), False))
        self.db.commit()
        cur.close()
