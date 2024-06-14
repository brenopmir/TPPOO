from tkinter import *
import customtkinter
import os 
import sys
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

class DispositivoAddFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color = "#616D7A",
                       width = 390,
                       corner_radius = 0,
                       height = 604,
                       )
        self.input = customtkinter.CTkEntry(self,placeholder_text="Digite o nome do dispositivo",
                                            height= 40, 
                                            width= 230,
                                            text_color="#000000")
        self.input.pack(side = "top", pady = 20)
        self.submit = customtkinter.CTkButton(self, text="Adicionar",
                                              text_color="#000000",
                                              fg_color = "#E4E4E4",
                                              hover_color="#E4E4E4")
        self.submit.pack(side = "top", pady = 5)

    #pegar dados do input input.get()
        
    
        
        
            
            
        
