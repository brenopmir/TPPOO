from tkinter import *
import customtkinter
import os 
import sys
from PIL import Image, ImageTk
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

class BotaoComodo(customtkinter.CTkButton):
    def __init__(self, master,nomeComodo, numeroDispositivos):
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
        
        imagem = Image.open("src/icons/sofa.png")
        imagem = imagem.resize((25,25))
        icone = ImageTk.PhotoImage(imagem)
        
        self.iconeLabel = customtkinter.CTkLabel(self.container, 
                                                 image=icone, 
                                                 text='',
                                                 width= 25,
                                                 height=25,
                                                 fg_color = "#E4E4E4")
        self.iconeLabel.image = icone 
        self.iconeLabel.grid(row=1, column=0,ipady=5)
        
        self.NomeLabel = customtkinter.CTkLabel(self, text=nomeComodo,
                                                font=("Inika", 20),
                                             text_color="#000000")
        self.NomeLabel.grid(row=0, column=0, pady=(10,0))
        
        
        self.dispositivosLabel = customtkinter.CTkLabel(self.container, text=f"{numeroDispositivos} dispositivos disponíveis",
                                                  font=("Inika", 12), text_color="#393939")
        self.dispositivosLabel.grid(row=1, column=1,padx= (10,0))
        

    #     self.bind("<Enter>", self.on_enter)
    #     self.bind("<Leave>", self.on_leave)
        
    #     self.iconeLabel.bind("<Enter>", self.on_enter)
    #     self.iconeLabel.bind("<Leave>", self.on_leave)
        
    #     self.NomeLabel.bind("<Enter>", self.on_enter)
    #     self.NomeLabel.bind("<Leave>", self.on_leave)
        
    #     self.dispositivosLabel.bind("<Enter>", self.on_enter)
    #     self.dispositivosLabel.bind("<Leave>", self.on_leave)

    # def on_enter(self, event):
    #      self.NomeLabel.configure(fg_color="#CCCCCC")
    #      self.dispositivosLabel.configure(fg_color="#CCCCCC")
    #      self.iconeLabel.configure(fg_color = "#CCCCCC")

    # def on_leave(self, event):
    #      self.NomeLabel.configure(fg_color="#E4E4E4")
    #      self.dispositivosLabel.configure(fg_color="#E4E4E4")
    #      self.iconeLabel.configure(fg_color = "#E4E4E4")
