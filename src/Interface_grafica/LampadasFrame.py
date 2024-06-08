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

class LampadasFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color = "#616D7A",
                       width = 390,
                       corner_radius = 0,
                       height = 604,
                       )
        self.header = HeaderDispositivo(master = self, texto = "Lâmpadas", caminho= "src/icons/lampada.png")
        self.header.pack(side="top", pady = (0,10),fill = "x",)