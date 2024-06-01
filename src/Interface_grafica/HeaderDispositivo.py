from tkinter import *
import customtkinter
import os 
import sys
from PIL import Image, ImageTk
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

class Header(customtkinter.CTkFrame):
    def __init__(self, master, texto,**kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color = "#DDDDDD",
                       width = 390,
                       corner_radius = 0,
                       height = 60)
        imagem = Image.open("src/icons/casa_icone.png")
        icone = ImageTk.PhotoImage(imagem)
        
        self.iconeLabel = customtkinter.CTkLabel(self,text='', image=icone,height= 60)
        self.iconeLabel.image = icone
        self.iconeLabel.pack(side="left",ipadx = 30)
        
        self.tituloLabel = customtkinter.CTkLabel(self, text=texto,
                                                   font=("Inika", 25),
                                                   text_color= "#000000")
        self.tituloLabel.pack(side="left", padx = 30)