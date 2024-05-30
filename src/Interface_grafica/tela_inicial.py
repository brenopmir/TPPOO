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
from Interface_grafica.BotaoComodo import BotaoComodo


#customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Automação Residencial')
        self.geometry('390x644')
        self.configure(fg_color ="#616D7A")
        self.header = Header(master = self)
        self.header.pack(side="top", fill = "x")
        
        self.BotaoComodo = BotaoComodo(master = self,
                                       nomeComodo="Quarto",
                                       )
        self.BotaoComodo.pack(side="top", pady= (25,10))
        self.BotaoComodo = BotaoComodo(master = self,
                                       nomeComodo="Cozinha",
                                       )
        self.BotaoComodo.pack(side="top", pady= 10)
        
        self.BotaoComodo = BotaoComodo(master = self,
                                       nomeComodo="Sala",
                                       )
        self.BotaoComodo.pack(side="top", pady= 10)
        
        self.BotaoComodo = BotaoComodo(master = self,
                                       nomeComodo="Sala",
                                       )
        self.BotaoComodo.pack(side="top", pady= 10)
        self.BotaoComodo = BotaoComodo(master = self,
                                       nomeComodo="    Sala",
                                       )
        self.BotaoComodo.pack(side="top", pady= 10)
        #self.teste = customtkinter.CTkButton(self, text="Hello world", fg_color="#E4E4E4", text_color="#000000",
                           #     hover_color="#000000")
        #self.teste.pack(pady = 20)
        
     
app = App()
app.mainloop()