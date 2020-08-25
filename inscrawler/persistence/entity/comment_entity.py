from peewee import AutoField, TextField, BigIntegerField, BooleanField, ForeignKeyField

from inscrawler.persistence.entity.base_model import BaseModel
from inscrawler.persistence.entity.post_entity import PostEntity
from inscrawler.persistence.entity.profile_entity import ProfileEntity


# TODO create indexes
class CommentEntity(BaseModel):
    id = AutoField()
    post = ForeignKeyField(PostEntity)
    author = ForeignKeyField(ProfileEntity)
    comment = TextField(null=True)
    last_visit = BigIntegerField(null=True)
    comment_date = BigIntegerField(null=True)
    deleted = BooleanField(null=True)

    class Meta:
        table_name = 'comment'
