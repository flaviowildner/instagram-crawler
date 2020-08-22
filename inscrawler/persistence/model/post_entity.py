from peewee import AutoField, TextField, BigIntegerField, BooleanField, ForeignKeyField

from inscrawler.persistence.model.base_model import BaseModel
from inscrawler.persistence.model.profile_entity import ProfileEntity


class PostEntity(BaseModel):
    id = AutoField()
    profile = ForeignKeyField(ProfileEntity)
    url = TextField()
    url_imgs = TextField()
    post_date = BigIntegerField()
    caption = TextField()
    last_visit = BigIntegerField()
    created_at = BigIntegerField()
    deleted = BooleanField()

    class Meta:
        table_name = 'post'
