from peewee import BigIntegerField, BooleanField, ForeignKeyField, CompositeKey

from inscrawler.repository import Comment
from inscrawler.repository.base_model import BaseModel
from inscrawler.repository.profile import Profile


class LikeOnComment(BaseModel):
    profile = ForeignKeyField(Profile)
    comment = ForeignKeyField(Comment)
    created_at = BigIntegerField()
    last_visit = BigIntegerField()
    deleted = BooleanField()

    class Meta:
        table_name = "like_on_comment"
        primary_key = CompositeKey('profile', 'comment')
