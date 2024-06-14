from tkinter import *
import customtkinter
import os 
import sys
from Interface_grafica.HeaderDispositivo import HeaderDispositivo
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

cores = ["Branco", "Amarelo", "Vermelho", "Azul", "Verde", "Roxo"]

class ConfigurarLampadas(customtkinter.CTkScrollableFrame):
    def __init__(self, master,nome,cor,intensidade, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color = "#616D7A",
                       width = 390,
                       corner_radius = 0,
                       height = 604,
                       )
        self.header = HeaderDispositivo(master = self, texto = nome, caminho= "src/icons/lampada.png")
        self.header.pack(side="top",fill = "x",)
        
        self.container1 = customtkinter.CTkFrame(self, fg_color="#E4E4E4")
        self.container1.pack(side="top",ipady = 5, ipadx=5, pady=(20,10))
        
        self.labelIntensidade = customtkinter.CTkLabel(self.container1, text=f"Intensidade: {intensidade}",
                                                font=("Inika", 20),
                                             text_color="#000000",
                                             bg_color="#E4E4E4")
        self.labelIntensidade.pack(side="top", pady=(20,10))
        
        self.slider = customtkinter.CTkSlider(master= self, from_=0, to=100,command= self.SetIntensidade,
                                              number_of_steps=100)
        self.slider.pack(side="top", pady=(10,10))
        self.slider.set(int(intensidade))
        
        self.container2 = customtkinter.CTkFrame(self, fg_color="#E4E4E4")
        self.container2.pack(side="top",pady=(20,10), padx=(10,10),ipady = 5, ipadx=5)
        
        self.labelCor = customtkinter.CTkLabel(self.container2, text=f"Cor: {cor}",
                                                font=("Inika", 20),
                                             text_color="#000000")
        self.labelCor.pack(side="top", pady=(10,10))
        
        self.select = customtkinter.CTkComboBox(master = self, values= cores,command=self.SetCor,
                                                width= 150, height = 50,font=("Inika",20))
        self.select.pack(side="top", pady=(10,10))
        
        self.excluir = customtkinter.CTkButton(self, text="Excluir Dispositivo",
                                              text_color="#FFFFFF",
                                              fg_color = "#C82E0D",
                                              hover_color="#C82E0D",
                                              height=50,
                                              width=150)
        self.excluir.pack(side = "top", pady = 80)
        
    def SetIntensidade(self,valor):
        #setar novo valor da intensidade no back
        self.labelIntensidade.configure(text = f"Intensidade: {valor}") 
        
    def SetCor(self,valor):
        #setar nova cor no back
        self.labelCor.configure(text = f"Cor: {valor}")