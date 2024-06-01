from tkinter import *
import customtkinter
import os 
import sys
from Interface_grafica.BotaoComodo import BotaoComodo
from Interface_grafica.HeaderDispositivo import Header
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
        self.header = Header(master = self, texto = nome)
        self.header.pack(side="top", pady = (0,10),fill = "x",)
        
        self.botaoLampada = BotaoDispositivo(self, nomeComodo="Lâmpadas",
                                  numeroDispositivos= len(nomeLampadas),
                                  caminho="src/icons/sofa.png")
        self.botaoLampada.pack(side="top", pady= (10,10))
            
        self.botaoAr = BotaoDispositivo(self, nomeComodo="Ar Condicionado",
                                  numeroDispositivos= 2,
                                  caminho="src/icons/sofa.png")
        self.botaoAr.pack(side="top", pady= (10,10))
        
        self.botaoJanela = BotaoDispositivo(self, nomeComodo="Janela",
                                  numeroDispositivos= len(nomeLampadas),
                                  caminho="src/icons/sofa.png")
        self.botaoJanela.pack(side="top", pady= (10,10))
        
        self.botaoCortina = BotaoDispositivo(self, nomeComodo="Cortina",
                                  numeroDispositivos= len(nomeLampadas),
                                  caminho="src/icons/sofa.png")
        
        self.botaoCortina.pack(side="top", pady= (10,10))
