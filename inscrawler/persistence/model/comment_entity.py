from peewee import AutoField, TextField, BigIntegerField, BooleanField, ForeignKeyField

from inscrawler.persistence.model.base_model import BaseModel
from inscrawler.persistence.model.post_entity import PostEntity
from inscrawler.persistence.model.profile_entity import ProfileEntity


# TODO create indexes
class CommentEntity(BaseModel):
    id = AutoField()
    post = ForeignKeyField(PostEntity)
    author = ForeignKeyField(ProfileEntity)
    comment = TextField()
    last_visit = BigIntegerField()
    comment_date = BigIntegerField()
    deleted = BooleanField()

    class Meta:
        table_name = 'comment'
