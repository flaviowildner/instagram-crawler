from inscrawler.persistence.model import *
from inscrawler.persistence.model.base_model import psql_db
from inscrawler.persistence.model.comment_entity import CommentEntity
from inscrawler.persistence.model.following_entity import FollowingEntity
from inscrawler.persistence.model.like_on_comment_entity import LikeOnCommentEntity
from inscrawler.persistence.model.like_on_post_entity import LikeOnPost
from inscrawler.persistence.model.post_entity import PostEntity
from inscrawler.persistence.model.profile_entity import ProfileEntity


def reset_db():
    psql_db.drop_tables([ProfileEntity, PostEntity, CommentEntity, LikeOnPost, LikeOnCommentEntity, FollowingEntity], cascade=True)

    ProfileEntity.create_table()
    PostEntity.create_table()
    CommentEntity.create_table()
    LikeOnPost.create_table()
    LikeOnCommentEntity.create_table()
    FollowingEntity.create_table()

# Uncomment to re-create tables
# reset_db()