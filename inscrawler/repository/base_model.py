from peewee import PostgresqlDatabase, Model

psql_db = PostgresqlDatabase('instagram-crawler', user='postgres', password='postgres', host='localhost')


class BaseModel(Model):
    class Meta:
        database = psql_db
