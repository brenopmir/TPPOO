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
from Interface_grafica.DispositivosFrame import DispositivosFrame
from Interface_grafica.BotaoComodo import BotaoComodo

nomeComodos = [("Quarto","9"), ("Cozinha","8"),("Sala","8"),("Quarto2","9")]
nomeLampadas = [("Lampada","9"), ("Lampada2","9"), ("Lampada3","9")]
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Automação Residencial')
        self.geometry('390x644')
        self.configure(fg_color ="#616D7A")
        self.dispositivosFrame = {}
        self.botoesComodo = {}
        self.comodoFrame = ComodoFrame(self)
        self.comodoFrame.pack(side= "top")

        for nomes,numero in nomeComodos:
            dispositivoFrame = DispositivosFrame(master = self, nome = nomes)
            self.dispositivosFrame[nomes] = dispositivoFrame
            dispositivoFrame.header.iconeBotao.configure(command = lambda: self.VoltarFrameComodos())
            
            self.botoesComodo[nomes] = BotaoComodo(self.comodoFrame, nomeComodo=nomes, numeroDispositivos=numero)
            self.botoesComodo[nomes].configure(command = lambda n=nomes:self.MudarFrameDispositivos(n))
            self.botoesComodo[nomes].pack(side="top", pady= (10,10))
               
        self.butao = customtkinter.CTkButton(self)
        
    def MudarFrameDispositivos(self,nome):
        self.comodoFrame.pack_forget()
        self.dispositivosFrame[nome].pack(side = "top")
        self.frameAtual = nome
        
    def VoltarFrameComodos(self):
        self.dispositivosFrame[self.frameAtual].pack_forget()
        self.comodoFrame.pack(side ='top')
     
app = App()
app.mainloop()