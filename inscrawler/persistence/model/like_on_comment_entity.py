from peewee import BigIntegerField, BooleanField, ForeignKeyField, CompositeKey

from inscrawler.persistence.model.base_model import BaseModel
from inscrawler.persistence.model.comment_entity import CommentEntity
from inscrawler.persistence.model.profile_entity import ProfileEntity


class LikeOnCommentEntity(BaseModel):
    profile = ForeignKeyField(ProfileEntity)
    comment = ForeignKeyField(CommentEntity)
    created_at = BigIntegerField()
    last_visit = BigIntegerField()
    deleted = BooleanField()

    class Meta:
        table_name = "like_on_comment"
        primary_key = CompositeKey('profile', 'comment')
