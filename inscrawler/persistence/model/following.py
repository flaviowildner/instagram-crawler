from peewee import BigIntegerField, BooleanField, ForeignKeyField, CompositeKey

from inscrawler.persistence.model.base_model import BaseModel
from inscrawler.persistence.model.profile import Profile


class Following(BaseModel):
    followed = ForeignKeyField(Profile)
    follower = ForeignKeyField(Profile)
    created_at = BigIntegerField()
    last_visit = BigIntegerField()
    deleted = BooleanField()

    class Meta:
        primary_key = CompositeKey('followed', 'follower')
