from peewee import AutoField, TextField, IntegerField, BigIntegerField, BooleanField

from inscrawler.persistence.model.base_model import BaseModel


# TODO create indexes
class ProfileEntity(BaseModel):
    id = AutoField()
    username = TextField()
    name = TextField()
    description = TextField()
    n_followers = IntegerField()
    n_following = IntegerField()
    n_posts = IntegerField()
    photo_url = TextField()
    last_visit = BigIntegerField()
    created_at = BigIntegerField()
    deleted = BooleanField()
    visited = BooleanField()

    class Meta:
        table_name = 'profile'
