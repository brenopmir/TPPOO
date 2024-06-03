from tkinter import *
import customtkinter
import os 
import sys
from PIL import Image, ImageTk
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

class HeaderDispositivo(customtkinter.CTkFrame):
    def __init__(self, master, texto,caminho,**kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color = "#DDDDDD",
                       width = 390,
                       corner_radius = 0,
                       height = 60)
        imagem = Image.open(caminho)
        imagem = imagem.resize((50,50))
        icone = ImageTk.PhotoImage(imagem)
        
        self.iconeBotao = customtkinter.CTkButton(self,fg_color = "#DDDDDD",
                                                  hover_color="#DDDDDD",
                                                  text='', 
                                                  image=icone,
                                                  height= 60)
        self.iconeBotao.image = icone
        self.iconeBotao.pack(side="left")
        
        self.tituloLabel = customtkinter.CTkLabel(self, text=texto,
                                                   font=("Inika", 25),
                                                   text_color= "#000000")
        self.tituloLabel.pack(side="left", padx = 10)