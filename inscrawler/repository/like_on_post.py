from peewee import BigIntegerField, BooleanField, ForeignKeyField, CompositeKey

from inscrawler.repository.base_model import BaseModel
from inscrawler.repository.post import Post
from inscrawler.repository.profile import Profile


class LikeOnPost(BaseModel):
    profile = ForeignKeyField(Profile)
    post = ForeignKeyField(Post)
    created_at = BigIntegerField()
    last_visit = BigIntegerField()
    deleted = BooleanField()

    class Meta:
        table_name = "like_on_post"
        primary_key = CompositeKey('profile', 'post')
