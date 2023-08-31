# models.py

from peewee import Model, SqliteDatabase, CharField, TextField, DateTimeField
from datetime import datetime

database = SqliteDatabase('my_todo.db')

class BaseModel(Model):
    class Meta:
        database = database

class TimeStampedModel(BaseModel):
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

class TodoItem(TimeStampedModel):
    task = CharField()
    description = TextField(null=True)
