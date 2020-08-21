from peewee import AutoField, TextField, BigIntegerField, BooleanField, ForeignKeyField

from inscrawler.repository.base_model import BaseModel
from inscrawler.repository.post import Post
from inscrawler.repository.profile import Profile


class Comment(BaseModel):
    id = AutoField()
    post = ForeignKeyField(Post)
    author = ForeignKeyField(Profile)
    comment = TextField()
    last_visit = BigIntegerField()
    comment_date = BigIntegerField()
    deleted = BooleanField()
