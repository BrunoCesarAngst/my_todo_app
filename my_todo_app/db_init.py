# db_init.py

from peewee import SqliteDatabase
from models import TodoItem

database = SqliteDatabase('my_todo.db')


def initialize_db():
    with database:
        database.create_tables([TodoItem])
