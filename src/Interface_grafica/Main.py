from tkinter import *
from typing import Tuple
import customtkinter
import os
import sys
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)
from Interface_grafica.HeaderFrame import Header
from Interface_grafica.ComodoFrame import ComodoFrame
from Interface_grafica.DispositivosFrame import DispositivosFrame
from Interface_grafica.BotaoComodo import BotaoComodo
from Interface_grafica.LampadasFrame import LampadasFrame
from Interface_grafica.BotaoLampada import BotaoLampada
from Interface_grafica.BotaoDispositivos import BotaoDispositivo
from Interface_grafica.ArCondicionadoFrame import ArCondicionadoFrame
from Interface_grafica.BotaoArCondicionado import BotaoArCondicionado
from Interface_grafica.JanelaFrame import JanelaFrame
from Interface_grafica.BotaoJanela import BotaoJanela
from Interface_grafica.CortinaFrame import CortinaFrame
from Interface_grafica.BotaoCortina import BotaoCortina

nomeComodos = [("Quarto","9"), ("Cozinha","8"),("Sala","8"),("Quarto2","9")]
#formato: (Comodo,Nome,Ligado,Temperatura,Intensidade,Abertura,Trancado,Cor)
nomeLampadas = [("Quarto","Lampada","","","50","","","Azul"),
                ("Quarto","Lampada2","","","60","","","Verde"),
                ("Cozinha","Lampada3","","","100","","","Rosa"),
                ("Sala","Lampada4","","","100","","","Amarelo")]

nomeArCondicionado = [("Quarto","ArCondicionado1",True,"20","50","","",""),
                     ("Quarto","ArCondicionado2",True,"25","60","","",""),
                     ("Cozinha","ArCondicionado3",False,"22","100","","",""),
                     ("Sala","ArCondicionado4",True,"12","100","","","")]

nomeJanelas =       [("Quarto","Janela1","","","50","",True,""),
                     ("Quarto","Janela2","","","60","",False,""),
                     ("Cozinha","Janela3","","","100","",False,""),
                     ("Sala","Janela4","","","100","",True,"")]

nomeCortina=        [("Quarto","Cortina1","","","","20","",""),
                     ("Quarto","Cortina2","","","","30","",""),
                     ("Cozinha","Cortina3","","","","50","",""),
                     ("Sala","Cortina4","","","","100","","")]
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Automação Residencial')
        self.geometry('390x644')
        self.configure(fg_color ="#616D7A")
        self.dispositivosFrame = {}
        self.lampadasFrame ={}
        self.lampadasBotoes = {}
        self.ArCondicionadoFrame = {}
        self.ArCondicionadoBotoes = {}
        self.janelaFrame = {}
        self.janelaBotoes = {}
        self.cortinasFrame ={}
        self.cortinasBotoes = {}
        self.botoesComodo = {}
        self.comodoFrame = ComodoFrame(self)
        self.comodoFrame.pack(side= "top")

        for nomes,numero in nomeComodos:
            contadorLampada = 0
            contadorArCondicionado = 0
            contadorJanela = 0
            contadorCortina = 0
            
            dispositivoFrame = DispositivosFrame(master = self, nome = nomes)
            self.dispositivosFrame[nomes] = dispositivoFrame
            dispositivoFrame.header.iconeBotao.configure(command = lambda: self.VoltarFrameComodos())
            
            lampadaFrame = LampadasFrame(master=self)
            lampadaFrame.header.iconeBotao.configure(command = lambda n=nomes: self.VoltarFrameDispositivosLampadas(n))
            self.lampadasFrame[nomes] = lampadaFrame
            
            for comodo,nome,ligado,temperatura,intensidade,abertura,tranca,cor in nomeLampadas:
                if comodo == nomes:
                    contadorLampada += 1
                    self.lampadasBotoes[nome] = BotaoLampada(self.lampadasFrame[nomes],
                                                             nomeLampada=nome,
                                                             cor=cor,
                                                             intensidade=intensidade)
                    #self.lampadasBotoes[nome].configure(command = lambda n=nomes:self.MudarFrameDispositivos(n))
                    self.lampadasBotoes[nome].pack(side="top", pady= (10,10))
             
            arCondicionadoFrame = ArCondicionadoFrame(master=self)
            arCondicionadoFrame.header.iconeBotao.configure(command = lambda n=nomes: self.VoltarFrameDispositivosAr(n))
            self.ArCondicionadoFrame[nomes] = arCondicionadoFrame
             
            for comodo,nome,ligado,temperatura,intensidade,abertura,tranca,cor in nomeArCondicionado:
                if comodo == nomes:
                    contadorArCondicionado += 1
                    self.ArCondicionadoBotoes[nome] = BotaoArCondicionado(self.ArCondicionadoFrame[nomes],
                                                             nomeAr=nome,
                                                             ligado=ligado,
                                                             temperatura=temperatura,
                                                             intensidade=intensidade)
                    #self.arCondicionadoBotoes[nome].configure(command = lambda n=nomes:self.MudarFrameDispositivos(n))
                    self.ArCondicionadoBotoes[nome].pack(side="top", pady= (10,10))
                    
            janelaFrame = JanelaFrame(master=self)
            janelaFrame.header.iconeBotao.configure(command = lambda n=nomes: self.VoltarFrameDispositivosJanela(n))
            self.janelaFrame[nomes] = janelaFrame
             
            for comodo,nome,ligado,temperatura,intensidade,abertura,tranca,cor in nomeJanelas:
                if comodo == nomes:
                    contadorJanela += 1
                    self.janelaBotoes[nome] = BotaoJanela(self.janelaFrame[nomes],
                                                             nomeJanela=nome,
                                                             intensidade=intensidade,
                                                             trancado=tranca)
                    #self.janelaBotoes[nome].configure(command = lambda n=nomes:self.MudarFrameDispositivos(n))
                    self.janelaBotoes[nome].pack(side="top", pady= (10,10))
             
             
            cortinaFrame = CortinaFrame(master=self)
            cortinaFrame.header.iconeBotao.configure(command = lambda n=nomes: self.VoltarFrameDispositivosCortina(n))
            self.cortinasFrame[nomes] = cortinaFrame
                    
            for comodo,nome,ligado,temperatura,intensidade,abertura,tranca,cor in nomeCortina:
                if comodo == nomes:
                    contadorCortina += 1
                    self.cortinasBotoes[nome] = BotaoCortina(self.cortinasFrame[nomes],
                                                             nomeCortina=nome,
                                                             abertura=abertura)
                    #self.cortinasBotoes[nome].configure(command = lambda n=nomes:self.MudarFrameDispositivos(n))
                    self.cortinasBotoes[nome].pack(side="top", pady= (10,10))        
                           
                
            self.botaoLampada = BotaoDispositivo(self.dispositivosFrame[nomes], nomeComodo="Lâmpadas",
                                  numeroDispositivos= contadorLampada,
                                  caminho="src/icons/lampada.png")
            self.botaoLampada.configure(command = lambda n=nomes:self.MudarFrameLampadas(n))
            self.botaoLampada.pack(side="top", pady= (10,10))
            
            self.botaoAr = BotaoDispositivo(self.dispositivosFrame[nomes], nomeComodo="Ar Condicionado",
                                  numeroDispositivos= contadorArCondicionado,
                                  caminho="src/icons/arCondicionado.png")
            self.botaoAr.configure(command = lambda n=nomes:self.MudarFrameAr(n))
            self.botaoAr.pack(side="top", pady= (10,10))
        
            self.botaoJanela = BotaoDispositivo(self.dispositivosFrame[nomes], nomeComodo="Janela",
                                  numeroDispositivos= contadorJanela,
                                  caminho="src/icons/Janela.png")
            self.botaoJanela.configure(command = lambda n=nomes:self.MudarFrameJanela(n))
            self.botaoJanela.pack(side="top", pady= (10,10))
        
            self.botaoCortina = BotaoDispositivo(self.dispositivosFrame[nomes], nomeComodo="Cortina",
                                  numeroDispositivos= contadorCortina,
                                  caminho="src/icons/cortina.png")
            self.botaoCortina.configure(command = lambda n=nomes:self.MudarFrameCortina(n))
            self.botaoCortina.pack(side="top", pady= (10,10))
            
            self.botoesComodo[nomes] = BotaoComodo(self.comodoFrame, nomeComodo=nomes, numeroDispositivos=numero)
            self.botoesComodo[nomes].configure(command = lambda n=nomes:self.MudarFrameDispositivos(n))
            self.botoesComodo[nomes].pack(side="top", pady= (10,10))
               
        
    def MudarFrameDispositivos(self,nome):
        self.comodoFrame.pack_forget()
        self.update()
        self.dispositivosFrame[nome].pack(side = "top")
        self.dispositivosFrame[nome].update()
        self.frameAtual = nome
        
    def VoltarFrameComodos(self):
        self.dispositivosFrame[self.frameAtual].pack_forget()
        self.update()
        self.comodoFrame.pack(side ='top')
        self.comodoFrame.update()
     
    def MudarFrameLampadas(self,nome):
        self.dispositivosFrame[self.frameAtual].pack_forget()
        self.update()
        self.lampadasFrame[nome].pack(side ='top')
        self.lampadasFrame[nome].update()
        self.frameAtual = nome
        self.update()
        
    def VoltarFrameDispositivosLampadas(self,nome):
        self.lampadasFrame[self.frameAtual].pack_forget()
        self.update()
        self.dispositivosFrame[nome].pack(side='top')
        self.dispositivosFrame[nome].update()
        self.update()
        self.frameAtual = nome
        
    def MudarFrameAr(self,nome):
        self.dispositivosFrame[self.frameAtual].pack_forget()
        self.update()
        self.ArCondicionadoFrame[nome].pack(side ='top')
        self.ArCondicionadoFrame[nome].update()
        self.frameAtual = nome
        self.update()
        
    def VoltarFrameDispositivosAr(self,nome):
        self.ArCondicionadoFrame[self.frameAtual].pack_forget()
        self.update()
        self.dispositivosFrame[nome].pack(side='top')
        self.dispositivosFrame[nome].update()
        self.update()
        self.frameAtual = nome    
         
    def MudarFrameJanela(self,nome):
        self.dispositivosFrame[self.frameAtual].pack_forget()
        self.update()
        self.janelaFrame[nome].pack(side ='top')
        self.janelaFrame[nome].update()
        self.frameAtual = nome
        self.update()
        
    def VoltarFrameDispositivosJanela(self,nome):
        self.janelaFrame[self.frameAtual].pack_forget()
        self.update()
        self.dispositivosFrame[nome].pack(side='top')
        self.dispositivosFrame[nome].update()
        self.update()
        self.frameAtual = nome   
    
    def MudarFrameCortina(self,nome):
        self.dispositivosFrame[self.frameAtual].pack_forget()
        self.update()
        self.cortinasFrame[nome].pack(side ='top')
        self.cortinasFrame[nome].update()
        self.frameAtual = nome
        self.update()
        
    def VoltarFrameDispositivosCortina(self,nome):
        self.cortinasFrame[self.frameAtual].pack_forget()
        self.update()
        self.dispositivosFrame[nome].pack(side='top')
        self.dispositivosFrame[nome].update()
        self.update()
        self.frameAtual = nome     
        
            
app = App()
app.mainloop()