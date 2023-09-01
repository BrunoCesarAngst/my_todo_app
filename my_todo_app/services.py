# services.py

from models import TodoItem
from datetime import datetime
import logging


class CustomException(Exception):
    def __init__(self, message, code=400):
        super().__init__(message)
        self.code = code

class TaskService:
    @staticmethod
    def add_task(task_text, description=None):
        try:
            TodoItem.create(task=task_text, description=description, created_at=datetime.now(), updated_at=datetime.now())
            return True
        except Exception as e:
            logging.error(f"Erro ao adicionar tarefa: {e}")
            raise CustomException("Erro ao adicionar tarefa")

    @staticmethod
    def delete_task(task_id):
        try:
            task = TodoItem.get_by_id(task_id)
            task.delete_instance()
            return True
        except Exception as e:
            logging.error(f"Erro ao deletar tarefa: {e}")
            raise CustomException("Erro ao deletar tarefa")

    @staticmethod
    def get_all_tasks():
        try:
            tasks = TodoItem.select()
            task_list = []
            for task in tasks:
                task_data = {
                    'id': task.id,
                    'task': task.task,
                    'description': task.description,
                    'created_at': task.created_at,
                    'updated_at': task.updated_at
                }
                task_list.append(task_data)
            return task_list
        except Exception as e:
            logging.error(f"Erro ao listar tarefas: {e}")
            raise CustomException("Erro ao listar tarefas")

    @staticmethod
    def get_task(task_id):
        try:
            task = TodoItem.get_by_id(TodoItem.id == task_id)
            return task
        except Exception as e:
            logging.error(f"Erro ao listar tarefas: {e}")
            raise CustomException("Erro ao listar tarefas")

    @staticmethod
    def save_task_changes(task_instance):
        task_instance.updated_at = datetime.now()
        return task_instance.save()

    @staticmethod
    def edit_task(task_id, new_content):
        task_to_edit = TaskService.get_task(task_id)
        if not task_to_edit:
            raise CustomException("Tarefa não encontrada")

        task_to_edit.task = new_content
        return TaskService.save_task_changes(task_to_edit)

    @staticmethod
    def list_tasks():
        try:
            return [(task.task, task.description, task.created_at, task.updated_at) for task in TodoItem.select()]
        except Exception as e:
            logging.error(f"Erro ao listar tarefas: {e}")
            raise CustomException("Erro ao listar tarefas")

    @staticmethod
    def update_task(task_id, new_task_text, new_description=None):
        try:
            task = TodoItem.get_by_id(task_id)
            task.task = new_task_text
            task.description = new_description
            task.updated_at = datetime.now()
            task.save()
            return True
        except Exception as e:
            logging.error(f"Erro ao atualizar tarefa: {e}")
            raise CustomException("Erro ao atualizar tarefa")
