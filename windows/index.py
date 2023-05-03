import os
import tkinter as tk
from kernel.directory import DESKTOP_PATH, create_file_log_task
from tkinter import ttk
from threading import Thread
from windows.task_one import TaskOne
from windows.task_two import TaskTwo
from add_on import labels
from automation.bot_one import bot_run


class Index(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Make Tasks')
        self.geometry('350x500')
        
        # criação do frame para escolher o tipo da tarefa
        self.type_task_frame = tk.Frame(self)
        self.type_task_frame.pack(side='top', fill='both', pady=10)

        # Criação da estrutura de widgets
        self.task_options = ['', 'TASK ONE', 'TASK TWO']
        self.selected_task = tk.StringVar()
        self.selected_task.set(self.task_options[0])
        self.lbl_info = tk.Label(self.type_task_frame, text='Tipo de Tarefa:')
        self.task_combobox = ttk.Combobox(self.type_task_frame, values=self.task_options, textvariable=self.selected_task)
        self.task_combobox.bind('<<ComboboxSelected>>', self.run_selected_task)
        
        # # Criação do frame para dos dados
        self.data_frame = tk.Frame(self)
        self.data_frame.pack(side='bottom', fill='both')

        # Criação do frame para as tarefas
        self.task_frame = tk.Frame(self)
        self.task_frame.pack(side='bottom', fill='both', expand=True)

        # Criação da lista de frames para as tarefas
        self.task_frames = []

        # Posicionamento dos widgets
        self.lbl_info.pack(side='left', padx=10)
        self.task_combobox.pack(side='left')
        
        # criação das tabelas
        
        self.table = ttk.Treeview(self.task_frame, columns=("id", "tarefa", "estado"), show="headings")
        self.table.pack(fill="both", expand=True)
        self.table.heading('id', text='ID', anchor="w")
        self.table.heading('tarefa', text='Tarefa', anchor="w")
        self.table.heading('estado', text='Estado', anchor="w")
        self.table.column("id", anchor="w", width=50)
        self.table.column("tarefa", anchor="w", width=50)
        self.table.column("estado", anchor="w", width=50)

    def open_folder(self, task):
        bot_path = os.path.join(DESKTOP_PATH, "bot")
        task_folder_path = os.path.join(bot_path, task)
        log_file_path = os.path.join(task_folder_path, f"{task}.txt")
        pasta = os.path.dirname(log_file_path)
        os.system(f'start "" "{pasta}"')

    def run_selected_task(self, event):
        selected = self.selected_task.get()
        if selected == 'TASK ONE':
            self.data_frame.destroy()
            self.data_frame = labels.create_new_frame(self, 'left', None, 0, 10)
            TaskOne(self.init_task, self.data_frame)
        elif selected == 'TASK TWO':
            self.data_frame.destroy()
            self.data_frame = labels.create_new_frame(self, 'left', None, 0, 10)
            TaskTwo(self.init_task, self.data_frame)
        else:
            self.data_frame.destroy()

    def init_task(self, data_task: list):
        if not data_task:
            tk.messagebox.showerror("Erro", "Digite o texto da tarefa.")
            return
        
        
        self.table.insert("", "end", values=[
            data_task[0],
            data_task[1], 
            'Processando'
            ]
        )
        
        tarefa_thread = Thread(target=self.processar_tarefa, args=[data_task])
        tarefa_thread.start()

    def processar_tarefa(self, task):
        with create_file_log_task(task[1]) as log_file:
            bot_run(task=task, log_file=log_file)
        labels.update_status_in_table(self.table, task[0])
