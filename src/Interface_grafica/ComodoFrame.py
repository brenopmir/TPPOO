from tkinter import *
import customtkinter
import os 
import sys
from Interface_grafica.BotaoComodo import BotaoComodo
from Interface_grafica.HeaderFrame import Header
from Interface_grafica.DispositivosFrame import DispositivosFrame
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

nomeComodos = [("Quarto","9"), ("Cozinha","8"),("Quarto2","9"), ("Sala","8")]
lampadasQuarto = [("Lampada","9"), ("Lampada2","9")]
lampadasQuarto2 = [("Lampada","9"), ("Lampada2","9"), ("Lampada3","9")]

class ComodoFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color = "#616D7A",
                       width = 390,
                       corner_radius = 0,
                       height = 604,
                       )
        
        self.header = Header(master = self)
        self.header.pack(side="top", pady = (0,10),fill = "x",)
        self.dispositivosFrame = {}
        self.botoes = []

    
        
        
            
            
        
