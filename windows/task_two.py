import random
import tkinter as tk
from tkinter import ttk
from add_on import labels

class TaskTwo:
    def __init__(self, target, frame=None):
        self.frame_root = frame
        self.target = target

        # Criação da estrutura de widgets
        self.frame_input_1 = labels.create_new_frame(self.frame_root, 'top', 'both', 0, 10)
        self.lbl_campo_1 = tk.Label(self.frame_input_1, text='Campo 1:')
        self.lbl_campo_1.pack(side='left', padx=10)
        self.entry_campo_1 = tk.Entry(self.frame_input_1)
        self.entry_campo_1.pack(side='right', padx=10)
        
        self.frame_input_2 = labels.create_new_frame(self.frame_root, 'top', 'both', 0, 10)
        self.lbl_campo_2 = tk.Label(self.frame_input_2, text='Campo 2:')        
        self.lbl_campo_2.pack(side='left', padx=10)
        self.entry_campo_2 = tk.Entry(self.frame_input_2)
        self.entry_campo_2.pack(side='right', padx=10)
        
        self.frame_execute = labels.create_new_frame(self.frame_root, 'bottom', 'both', 0, 20)
        self.btn_executar = tk.Button(self.frame_execute, text='Executar', command=lambda: [self.target([
            random.randint(1000, 9999), 
            self.entry_campo_1.get(),
            self.entry_campo_2.get()])])

        self.btn_executar.pack(side='left', padx=10)
