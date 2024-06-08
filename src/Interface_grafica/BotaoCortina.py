from tkinter import *
import customtkinter
import os 
import sys
from PIL import Image, ImageTk
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

class BotaoCortina(customtkinter.CTkButton):
    def __init__(self, master,nomeCortina,abertura):
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
        
        imagem = Image.open("src/icons/abertura.png")
        imagem = imagem.resize((25,25))
        icone = ImageTk.PhotoImage(imagem)
        
        self.NomeLabel = customtkinter.CTkLabel(self, text=nomeCortina,
                                                font=("Inika", 20),
                                             text_color="#000000")
        self.NomeLabel.grid(row=0, column=0, pady=(10,0), padx=(15,0))
        
        self.icone1Label = customtkinter.CTkLabel(self.container, 
                                                 image=icone, 
                                                 text='',
                                                 width= 25,
                                                 height=25,
                                                 fg_color = "#E4E4E4")
        self.icone1Label.image = icone
        self.icone1Label.grid(row=1, column=0,ipady=5)
        
        self.AberturaLabel = customtkinter.CTkLabel(self.container, text=f"Abertura - {abertura}%",
                                                  font=("Inika", 12), text_color="#393939")
        self.AberturaLabel.grid(row=1, column=1,padx= (10,0))
        
        

