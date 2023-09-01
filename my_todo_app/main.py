# main.py

from kivy.app import App
from layouts import TodoLayout
from db_init import initialize_db


class TodoApp(App):
    def build(self):
        return TodoLayout()


if __name__ == '__main__':
    initialize_db()
    TodoApp().run()
