from peewee import AutoField, TextField, BigIntegerField, BooleanField, ForeignKeyField

from inscrawler.persistence.model.base_model import BaseModel
from inscrawler.persistence.model.profile import Profile


class Post(BaseModel):
    id = AutoField()
    profile = ForeignKeyField(Profile)
    url = TextField()
    url_imgs = TextField()
    post_date = BigIntegerField()
    caption = TextField()
    last_visit = BigIntegerField()
    created_at = BigIntegerField()
    deleted = BooleanField()
