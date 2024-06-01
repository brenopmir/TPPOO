from tkinter import *
from typing import Tuple
import customtkinter
import os
import sys
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)
from Interface_grafica.HeaderFrame import Header
from Interface_grafica.ComodoFrame import ComodoFrame

lampadasQuarto = [("Lampada","9"), ("Lampada2","9"), ("Lampada3","9")]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Automação Residencial')
        self.geometry('390x644')
        self.configure(fg_color ="#616D7A")
        
        self.comodoFrame = ComodoFrame(self)
        self.comodoFrame.pack(side="top", fill = "x")
        self.butao = customtkinter.CTkButton(self)
        
     
app = App()
app.mainloop()