from tkinter import *
import customtkinter
import os 
import sys
from Interface_grafica.BotaoComodo import BotaoComodo
from Interface_grafica.HeaderDispositivo import HeaderDispositivo
from Interface_grafica.BotaoDispositivos import BotaoDispositivo
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

nomeLampadas = [("Lampada","9"), ("Lampada2","9"), ("Lampada3","9")]

class DispositivosFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, nome, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color = "#616D7A",
                       width = 390,
                       corner_radius = 0,
                       height = 604,
                       )
        self.header = HeaderDispositivo(master = self, texto = nome, caminho= "src/icons/dispositivos.png")
        self.header.pack(side="top", pady = (0,10),fill = "x",)
        