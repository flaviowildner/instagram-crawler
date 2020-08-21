from peewee import AutoField, TextField, BigIntegerField, BooleanField, ForeignKeyField

from inscrawler.persistence.model.base_model import BaseModel
from inscrawler.persistence.model.post import Post
from inscrawler.persistence.model.profile import Profile


class Comment(BaseModel):
    id = AutoField()
    post = ForeignKeyField(Post)
    author = ForeignKeyField(Profile)
    comment = TextField()
    last_visit = BigIntegerField()
    comment_date = BigIntegerField()
    deleted = BooleanField()
