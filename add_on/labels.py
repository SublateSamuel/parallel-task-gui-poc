import tkinter as tk
from tkinter import ttk

def create_new_frame(task_frame, side, fill, padx, pady):
  task_frame = tk.Frame(task_frame)
  task_frame.pack(side=side, fill=fill, padx=padx, pady=pady)
  return task_frame

def new_frame_with_place(frame_root, relx, rely, anchor):
  frame = tk.Frame(frame_root)
  frame.place(relx=relx, rely=rely, anchor=anchor)
  return frame

def create_task_name_in_frame(task_frame, data_task):
  task_name = tk.Label(task_frame, text=data_task, width=10)
  task_name.pack(side='left')

def insert_progressbar_of_task(task_frame):
  task_bar = ttk.Progressbar(task_frame, style='TProgressbar', orient=tk.HORIZONTAL, mode='determinate', maximum=5)
  return task_bar
  
def insert_label_of_status_task(task_frame):
  task_status = tk.Label(task_frame, text='Processando')
  return task_status

def update_status_in_table(table, task_name):
  for row in table.get_children():
    if int(table.item(row, 'values')[0]) == task_name:
      table.set(row, 'estado', 'Concluida')

def insert_button_open_folder(table, open_folder, task):
  abrir_pasta_button = tk.Button(table, text="Abrir", command=lambda: open_folder(task))
  return abrir_pasta_button
  
def create_new_task_button(gui_implements, name_task, command):
  tk.Button(gui_implements, text=name_task, command=command)