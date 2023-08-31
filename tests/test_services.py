import pytest

from my_todo_app.services import add_task, list_tasks, update_task

@pytest.fixture
def prepare_tasks():
    add_task("Task 1", "Description 1")
    add_task("Task 2", "Description 2")
    add_task("Task 3", "Description 3")
    yield
    TodoItem.delete().execute()
