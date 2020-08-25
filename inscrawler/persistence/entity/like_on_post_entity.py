from peewee import BigIntegerField, BooleanField, ForeignKeyField, CompositeKey

from inscrawler.persistence.entity.base_model import BaseModel
from inscrawler.persistence.entity.post_entity import PostEntity
from inscrawler.persistence.entity.profile_entity import ProfileEntity


# TODO create indexes
class LikeOnPost(BaseModel):
    profile = ForeignKeyField(ProfileEntity)
    post = ForeignKeyField(PostEntity)
    created_at = BigIntegerField()
    last_visit = BigIntegerField()
    deleted = BooleanField()

    class Meta:
        table_name = "like_on_post"
        primary_key = CompositeKey('profile', 'post')
