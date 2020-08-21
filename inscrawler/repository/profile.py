from peewee import AutoField, TextField, IntegerField, BigIntegerField, BooleanField

from inscrawler.repository.base_model import BaseModel


class Profile(BaseModel):
    id = AutoField()
    username = TextField()
    description = TextField()
    n_followers = IntegerField()
    n_following = IntegerField()
    n_posts = IntegerField()
    photo_url = TextField()
    last_visit = BigIntegerField()
    created_at = BigIntegerField()
    deleted = BooleanField()
    visited = BooleanField()
