from peewee import BigIntegerField, BooleanField, ForeignKeyField, CompositeKey

from inscrawler.persistence.model.base_model import BaseModel
from inscrawler.persistence.model.profile_entity import ProfileEntity


class FollowingEntity(BaseModel):
    followed = ForeignKeyField(ProfileEntity)
    follower = ForeignKeyField(ProfileEntity)
    created_at = BigIntegerField()
    last_visit = BigIntegerField()
    deleted = BooleanField()

    class Meta:
        primary_key = CompositeKey('followed', 'follower')
        table_name = 'following'
