from tkinter import *
import customtkinter
import os 
import sys
from PIL import Image, ImageTk
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

class BotaoLampada(customtkinter.CTkButton):
    def __init__(self, master,nomeLampada, cor, intensidade):
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
        self.container.grid(row=1, column=0, padx=(0, 5), pady=10)
        
        imagem1 = Image.open("src/icons/Cor.png")
        imagem1 = imagem1.resize((25,25))
        icone1 = ImageTk.PhotoImage(imagem1)
        
        imagem2 = Image.open("src/icons/power.png")
        imagem2 = imagem2.resize((25,25))
        icone2 = ImageTk.PhotoImage(imagem2)
        
        self.NomeLabel = customtkinter.CTkLabel(self, text=nomeLampada,
                                                font=("Inika", 20),
                                             text_color="#000000")
        self.NomeLabel.grid(row=0, column=0, pady=(10,0), padx=(15,0))
        
        self.icone1Label = customtkinter.CTkLabel(self.container, 
                                                 image=icone1, 
                                                 text='',
                                                 width= 25,
                                                 height=25,
                                                 fg_color = "#E4E4E4")
        self.icone1Label.image = icone1 
        self.icone1Label.grid(row=1, column=0,ipady=5)
        
        self.corLabel = customtkinter.CTkLabel(self.container, text=cor,
                                                  font=("Inika", 12), text_color="#393939")
        self.corLabel.grid(row=1, column=1,padx= (10,0))
        
        self.icone2Label = customtkinter.CTkLabel(self.container, 
                                                 image=icone2, 
                                                 text='',
                                                 width= 25,
                                                 height=25,
                                                 fg_color = "#E4E4E4")
        self.icone2Label.image = icone2
        self.icone2Label.grid(row=2, column=0,ipady=5)
        
        self.intensidadeLabel = customtkinter.CTkLabel(self.container, text=f"{intensidade}%",
                                                  font=("Inika", 12), text_color="#393939")
        self.intensidadeLabel.grid(row=2, column=1,padx= (10,0))
        

