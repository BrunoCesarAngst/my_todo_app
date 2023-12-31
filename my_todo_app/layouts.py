# layouts.py

from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from services import TaskService  # Suppose you created a service class for task operations


class TodoLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(TodoLayout, self).__init__(**kwargs)  # Importante: chame o __init__ da classe mãe primeiro
        Clock.schedule_once(lambda dt: self.update_task_list(), 0)  # Agende a chamada de update_task_list

    def on_task_click(self, task_id):
        pop = Popup(title='Opções', size_hint=(None, None), size=(400, 400))

        box = BoxLayout(orientation='vertical')

        new_task_input = TextInput(
            hint_text='Atualizar tarefa',
            size_hint=(1, 0.2),
        )

        # Botão de deletar
        delete_button = Button(text='Deletar', size_hint=(1, 0.2))
        delete_button.bind(on_press=lambda x: self.delete_task(task_id, pop))

        # Botão de atualizar
        update_button = Button(text='Atualizar', size_hint=(1, 0.2))
        update_button.bind(on_press=lambda x: self.update_task(task_id, new_task_input.text, pop))

        box.add_widget(new_task_input)
        box.add_widget(delete_button)
        box.add_widget(update_button)

        pop.content = box

        pop.open()
        # pass

    def add_task(self):
        task = self.ids.task_input.text  # Pega o texto do TextInput
        description = self.ids.description_input.text  # Pega o texto do TextInput
        if TaskService.add_task(task, description):  # Usa a função do módulo de serviço para adicionar a tarefa
            self.update_task_list()  # Atualiza a lista de tarefas na interface do usuário
            self.ids.task_input.text = ''  # Limpa o TextInput
            self.ids.description_input.text = ''  # Limpa o TextInput
            self.ids.task_input.focus = True  # Retorna o foco para o TextInput

    def delete_task(self, task_id, popup_instance):
        sucess = TaskService.delete_task(task_id)  # Usa a função do módulo de serviço para deletar a tarefa
        if sucess:
            self.update_task_list()  # Atualiza a lista de tarefas na interface do usuário
            popup_instance.dismiss()  # Fecha o popup

    def update_task(self, task_id, new_task_text, popup_instance):
        sucess = TaskService.update_task(task_id, new_task_text)  # Usa a função do módulo de serviço para atualizar a tarefa
        if sucess:
            self.update_task_list()
            popup_instance.dismiss()

    def update_task_list(self):
        print("Limpando widgets antigos...")
        self.ids.task_list.clear_widgets()
        tasks = TaskService.get_all_tasks()  # Usa a função do módulo de serviço para listar as tarefas
        print(f"Adicionando {len(tasks)} novas tarefas.")
        for task in tasks:
            # print(task)
            task_button = Button(
                text=task['task'],
                on_press=lambda instace, task_id=task['id']: self.on_task_click(task_id))
            self.ids.task_list.add_widget(task_button)
        print("Widgets atualmente em task_list:", self.ids.task_list.children)

        self.ids.task_list.do_layout()
