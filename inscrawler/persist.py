from .database.postgres import connect
from datetime import datetime


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
                name TEXT NOT NULL,
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
                author INTEGER REFERENCES profile(id),
                comment TEXT,
                last_visit BIGINT,
                deleted BOOLEAN,
                PRIMARY KEY (id)
            );
            """
        ]
        cur = self.db.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        self.db.commit()

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
            id_profile = ids_profile[0]
        else:
            id_profile = None

        cur.close()

        return id_profile

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

# username, profile.name, profile.desc, profile.follower_num, profile.following,
        #    profile.post_num, profile.photo_url, int(datetime.now().timestamp()), int(datetime.now().timestamp())

    def persistPost(self, id_profile, url, url_imgs, post_date, caption, last_visit, deleted):
        if self.db is None:
            return
        sql = """
            INSERT INTO post(id_profile, url, url_imgs, post_date, caption, last_visit, deleted)
            VALUES(%s, %s, %s, %s, %s, %s, %s);
        """
        cur = self.db.cursor()
        cur.execute(sql, (id_profile, url, url_imgs, post_date,
                          caption, last_visit, deleted))
        self.db.commit()
        cur.close()

    def persistComment(self, id_post, author_id, comment, id_comment_reply, last_visit, deleted):
        if self.db is None:
            return
        sql = """
            INSERT INTO post(id_post, author_id, comment, last_visit, deleted)
            VALUES(%s, %s, %s, %s, %s);
        """
        cur = self.db.cursor()
        cur.execute(sql, (id_post, author_id, comment, last_visit, deleted))
        self.db.commit()
        cur.close()
