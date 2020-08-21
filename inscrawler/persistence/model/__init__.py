from inscrawler.persistence.model import *
from inscrawler.persistence.model.base_model import psql_db
from inscrawler.persistence.model.comment import Comment
from inscrawler.persistence.model.following import Following
from inscrawler.persistence.model.like_on_comment import LikeOnComment
from inscrawler.persistence.model.like_on_post import LikeOnPost
from inscrawler.persistence.model.post import Post
from inscrawler.persistence.model.profile import Profile


def reset_db():
    psql_db.drop_tables([Profile, Post, Comment, LikeOnPost, LikeOnComment, Following], cascade=True)

    Profile.create_table()
    Post.create_table()
    Comment.create_table()
    LikeOnPost.create_table()
    LikeOnComment.create_table()
    Following.create_table()

# Uncomment to re-create tables
# reset_db()
