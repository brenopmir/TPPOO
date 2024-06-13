from tkinter import *
import customtkinter
import os 
import sys
from Interface_grafica.HeaderDispositivo import HeaderDispositivo
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)


class ConfigurarCortina(customtkinter.CTkScrollableFrame):
    def __init__(self, master,nome,abertura, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color = "#616D7A",
                       width = 390,
                       corner_radius = 0,
                       height = 604,
                       )
        self.header = HeaderDispositivo(master = self, texto = nome, caminho= "src/icons/cortina.png")
        self.header.pack(side="top",fill = "x",)
        
        self.container1 = customtkinter.CTkFrame(self, fg_color="#E4E4E4")
        self.container1.pack(side="top",ipady = 5, ipadx=5, pady=(20,10))
        
        self.labelAbertura = customtkinter.CTkLabel(self.container1, text=f"Abertura: {abertura}",
                                                font=("Inika", 20),
                                             text_color="#000000",
                                             bg_color="#E4E4E4")
        self.labelAbertura.pack(side="top", pady=(20,10))
        
        self.slider = customtkinter.CTkSlider(master= self, from_=0, to=100,command= self.SetAbertura,
                                              number_of_steps=100)
        self.slider.pack(side="top", pady=(10,10))
        self.slider.set(int(abertura))
    
        self.excluir = customtkinter.CTkButton(self, text="Excluir Dispositivo",
                                              text_color="#FFFFFF",
                                              fg_color = "#C82E0D",
                                              hover_color="#C82E0D",
                                              height=50,
                                              width=150)
        self.excluir.pack(side = "top", pady = 80)
        
    def SetAbertura(self,valor):
        #setar novo valor da abertura no back
        self.labelAbertura.configure(text = f"Abertura: {valor}") 
        
