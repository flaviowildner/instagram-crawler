from peewee import BigIntegerField, BooleanField, ForeignKeyField, CompositeKey

from inscrawler.persistence.model.base_model import BaseModel
from inscrawler.persistence.model.post import Post
from inscrawler.persistence.model.profile import Profile


class LikeOnPost(BaseModel):
    profile = ForeignKeyField(Profile)
    post = ForeignKeyField(Post)
    created_at = BigIntegerField()
    last_visit = BigIntegerField()
    deleted = BooleanField()

    class Meta:
        table_name = "like_on_post"
        primary_key = CompositeKey('profile', 'post')
