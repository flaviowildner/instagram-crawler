from inscrawler.repository.base_model import *
from inscrawler.repository.comment import Comment
from inscrawler.repository.following import Following
from inscrawler.repository.like_on_comment import LikeOnComment
from inscrawler.repository.like_on_post import LikeOnPost
from inscrawler.repository.post import Post
from inscrawler.repository.profile import Profile


def reset_db():
    psql_db.drop_tables([Profile, Post, Comment, LikeOnPost, LikeOnComment, Following], cascade=True)

    Profile.create_table()
    Post.create_table()
    Comment.create_table()
    LikeOnPost.create_table()
    LikeOnComment.create_table()
    Following.create_table()


# Uncomment to re-create tables
reset_db()
