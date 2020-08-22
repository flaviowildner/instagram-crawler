from peewee import BigIntegerField, BooleanField, ForeignKeyField, CompositeKey

from inscrawler.persistence.model.base_model import BaseModel
from inscrawler.persistence.model.post_entity import PostEntity
from inscrawler.persistence.model.profile_entity import ProfileEntity


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
