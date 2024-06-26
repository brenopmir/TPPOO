from tkinter import *
import customtkinter
import os 
import sys
from Interface_grafica.HeaderDispositivo import HeaderDispositivo
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)


class ConfigurarAr(customtkinter.CTkScrollableFrame):
    def __init__(self,casas,comodo, master,nome,ligado,temperatura,intensidade, **kwargs):
        super().__init__(master, **kwargs)
        self.casa = casas
        self.comodo = comodo
        self.nome = nome
        self.ligado = ligado
        self.temperatura = temperatura
        self.intensidade = intensidade
        self.texto = "Ligado"
        if ligado == "True":
            self.texto = "Ligado"
        elif ligado == "False":
            self.texto = "Desligado"

        self.configure(fg_color = "#616D7A",
                       width = 390,
                       corner_radius = 0,
                       height = 604,
                       )
        self.header = HeaderDispositivo(master = self, texto = nome, caminho= "src/icons/arCondicionado.png")
        self.header.pack(side="top",fill = "x",)
        
        self.container1 = customtkinter.CTkFrame(self, fg_color="#E4E4E4")
        self.container1.pack(side="top",ipady = 5, ipadx=5, pady=(20,10))
        
        self.labelTemperatura = customtkinter.CTkLabel(self.container1, text=f"Temperatura: {temperatura}°C",
                                                font=("Inika", 20),
                                             text_color="#000000",
                                             bg_color="#E4E4E4")
        self.labelTemperatura.pack(side="top", pady=(20,10))
        
        self.slider1 = customtkinter.CTkSlider(master= self, from_=0, to=30,command= self.SetTemperatura,
                                              number_of_steps=30)
        self.slider1.pack(side="top", pady=(10,10))
        self.slider1.set(int(temperatura))
        
        self.container2 = customtkinter.CTkFrame(self, fg_color="#E4E4E4")
        self.container2.pack(side="top",ipady = 5, ipadx=5, pady=(20,10))
        
        self.labelIntensidade = customtkinter.CTkLabel(self.container2, text=f"Intensidade: {intensidade}",
                                                font=("Inika", 20),
                                             text_color="#000000",
                                             bg_color="#E4E4E4")
        self.labelIntensidade.pack(side="top", pady=(20,10))
        
        self.slider2 = customtkinter.CTkSlider(master= self, from_=0, to=100,command= self.SetIntensidade,
                                               number_of_steps=100)
        self.slider2.pack(side="top", pady=(10,10))
        self.slider2.set(int(intensidade))

        self.check = customtkinter.StringVar(value= ligado)
        self.checkBox = customtkinter.CTkCheckBox(self,variable= self.check,
                                                  onvalue="True", 
                                                  offvalue="False",
                                                  text= self.texto,
                                                  command= lambda:self.SetLigado(),
                                                  height= 40,
                                                  font=("Inika",20)
                                                  )
        self.checkBox.pack(side="top", pady=(10,10))
        
        self.excluir = customtkinter.CTkButton(self, text="Excluir Dispositivo",
                                              text_color="#FFFFFF",
                                              fg_color = "#C82E0D",
                                              hover_color="#C82E0D",
                                              height=50,
                                              width=150)
        self.excluir.pack(side = "top", pady = 80)
        
    def SetTemperatura(self,valor):
        self.temperatura = int(valor)
        self.labelTemperatura.configure(text = f"Temperatura: {valor}°C")
        self.SetarAr()
        
    def SetIntensidade(self,valor):
        self.intensidade = int(valor)
        self.labelIntensidade.configure(text = f"Intensidade: {valor}")  
        self.SetarAr()
        
    def SetLigado(self):
        self.ligado = self.check.get()
        if self.ligado == "True":
            self.texto = "Ligado"
        elif self.ligado == "False":
            self.texto = "Desligado"
        self.checkBox.configure(text = self.texto)
        self.SetarAr()
    
    def SetarAr(self):
        if self.ligado == "True":
            self.casa.comodos[self.comodo].ConfigurarArCondicionado(self.nome,"True",self.temperatura,self.intensidade)
        elif self.ligado == "False":
            self.casa.comodos[self.comodo].ConfigurarArCondicionado(self.nome,"False",self.temperatura,self.intensidade)