# utils.py

def format_tasks(tasks):
    """
    Formata uma lista de tarefas em uma lista de strings formatadas.

    Cada tarefa é uma tupla contendo: (nome da tarefa, descrição, data de criação, data de atualização).

    Retorna uma lista de strings, cada uma representando uma tarefa formatada.
    """
    task_template = """{}
 - Description: {}
 - Created at: {}
 - Updated at: {}"""

    return [task_template.format(name, description, created_at, updated_at) for name, description, created_at, updated_at in tasks]
