from tkinter import *
import customtkinter
import os 
import sys
from PIL import Image, ImageTk
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

class BotaoAdd(customtkinter.CTkButton):
    def __init__(self, master, label):
        super().__init__(master)
        self.configure(fg_color = "#E4E4E4",
                       hover_color="#E4E4E4",
                       height=60, 
                       width=280, 
                       corner_radius=15,
                       text='',
                       text_color="#000000",
                       font=("Inika",20),
                       compound = "left",
                       anchor ="top"
                       )
        self.container = customtkinter.CTkFrame(self, fg_color="#E4E4E4")
        self.container.grid(row=1, column=0, padx=(10, 5), pady=10)
        
        imagem = Image.open("src/icons/add.png")
        imagem = imagem.resize((25,25))
        icone = ImageTk.PhotoImage(imagem)
        
        self.iconeLabel = customtkinter.CTkLabel(self.container, 
                                                 image=icone, 
                                                 text='',
                                                 width= 25,
                                                 height=25,
                                                 fg_color = "#E4E4E4")
        self.iconeLabel.image = icone 
        self.iconeLabel.grid(row=0, column=0,ipady=5)
        
        
        self.AdicionarLabel = customtkinter.CTkLabel(self.container, text=label,
                                                  font=("Inika", 15), text_color="#000000")
        self.AdicionarLabel.grid(row=0, column=1,padx= (10,0))
        
