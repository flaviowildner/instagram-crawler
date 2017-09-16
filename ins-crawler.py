from browser import Browser
from time import sleep


class InsCrawler:
    URL = 'https://www.instagram.com/'

    def __init__(self,):
        self.browser = Browser()

    def get_user_profile(self, username):
        browser = self.browser
        browser.get('https://www.instagram.com/%s/' % username)
        name = browser.find_one('._kc4z2').text
        desc = browser.find_one('._tb97a span').text
        photo_url = browser.find_one('._9bt3u ').get_attribute('src')
        statistics = [int(ele.text) for ele in browser.find('._fd86t')]
        post_num, follower_num, following_num = statistics

        return {
            'name': name,
            'desc': desc,
            'photo_url': photo_url,
            'post_num': post_num,
            'follower_num': follower_num,
            'following_num': following_num
        }

    def _get_posts(self, num):
        '''
            To get posts, we have to click on the load more
            button and make the browser call post api.
        '''
        browser = self.browser
        more_btn = browser.find_one('._1cr2e._epyes')
        more_btn.click()

        ele_posts = []
        while len(ele_posts) < num:
            ele_posts = browser.find('._cmdpi ._mck9w')
            browser.scroll_down()
            sleep(0.2)

        posts = []
        for idx, ele in enumerate(ele_posts):
            if idx == num:
                break

            ele_img = browser.find_one('._2di5p', ele)
            content = ele_img.get_attribute('alt')
            img_url = ele_img.get_attribute('src')
            posts.append({
                'content': content,
                'img_url': img_url
            })

        return posts

    def get_user_posts(self, username):
        user_profile = self.get_user_profile(username)
        post_num = user_profile['post_num']
        return self._get_posts(post_num)

    def get_latest_posts_by_tag(self, tag, num):
        self.browser.get(
            'https://www.instagram.com/explore/tags/%s/' % tag)
        return self._get_posts(num)


if __name__ == '__main__':
    ins_crawler = InsCrawler()
    print(ins_crawler.get_user_profile('cal_foodie'))
    print(len(ins_crawler.get_latest_posts_by_tag('foodie', 10)))