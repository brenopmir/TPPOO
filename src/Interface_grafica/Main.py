from tkinter import *
from typing import Tuple
import customtkinter
import os
import sys
# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)
from objects.planilha import iniciar_planilhas
from openpyxl import load_workbook

casa_path = os.path.abspath("Casa.xlsx")
casa_comodos_path = os.path.abspath("Casa_comodos.xlsx")

if not (os.path.exists(casa_path)) and os.path.exists(os.path.dirname(casa_comodos_path)):
    iniciar_planilhas()

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
from Interface_grafica.BotaoAdd import BotaoAdd
from Interface_grafica.BotaoRemove import BotaoRemove
from Interface_grafica.ComodoRemoveFrame import ComodoRemoveFrame
from Interface_grafica.ConfigurarLampada import ConfigurarLampadas
from Interface_grafica.ConfigurarCortina import ConfigurarCortina
from Interface_grafica.ConfigurarJanela import ConfigurarJanela
from Interface_grafica.ConfigurarAr import ConfigurarAr
from Interface_grafica.DispostivoAdd import DispositivoAddFrame
from Interface_grafica.ComodoAddFrame import ComodoAddFrame
from objects.Casa import Casa
from objects.Comodo import Comodo
from objects.ArCondicionado import Ar_Condicionado,criar_instancia_ar_condicionado
from objects.Cortinas import Cortina,criar_instancia_cortina
from objects.Janelas import Janela,criar_instancia_janela
from objects.Lampadas import Lampadas,criar_instancia_lampada
from objects.Dispositivo import Dispositivo
from typing import Type


'''nomeComodos = [("Quarto","9"), ("Cozinha","8"),("Sala","8"),("Quarto2","9")]
#formato: (Comodo,Nome,Ligado,Temperatura,Intensidade,Abertura,Trancado,Cor)
nomeLampadas = [("Quarto","Lampada","","","50","","","Azul"),
                ("Quarto","Lampada2","","","60","","","Verde"),
                ("Cozinha","Lampada3","","","100","","","Rosa"),
                ("Sala","Lampada4","","","100","","","Amarelo")]

nomeArCondicionado = [("Quarto","ArCondicionado1","True","20","50","","",""),
                     ("Quarto","ArCondicionado2","True","25","60","","",""),
                     ("Cozinha","ArCondicionado3","False","22","100","","",""),
                     ("Sala","ArCondicionado4","True","12","100","","","")]

nomeJanelas =       [("Quarto","Janela1","","","","50","Trancado",""),
                     ("Quarto","Janela2","","","","60","Aberto",""),
                     ("Cozinha","Janela3","","","","100","False",""),
                     ("Sala","Janela4","","","","100","True","")]

nomeCortina=        [("Quarto","Cortina1","","","","20","",""),
                     ("Quarto","Cortina2","","","","30","",""),
                     ("Cozinha","Cortina3","","","","50","",""),
                     ("Sala","Cortina4","","","","100","","")]'''
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Automação Residencial')
        self.geometry('390x644')
        self.configure(fg_color ="#616D7A")
        self.casa = Casa("Casa")
        self.comodos = []
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
        self.lampadasConfig = {}
        self.arConfig = {}
        self.janelaConfig = {}
        self.cortinaConfig = {}
        self.frameAtual = ""
        self.comodoFrame = False
        self.CarregarVetores()
        self.CriarJanelas()
        
    def CarregarVetores(self):
        self.nomeComodos=[]
        self.nomeLampadas=[]
        self.nomeArCondicionado=[]
        self.nomeJanelas=[]
        self.nomeCortina=[]
        
        wb=load_workbook("Casa.xlsx")
        ws_lampadas=wb["Lampadas"]
        ws_cortinas=wb["Cortinas"]
        ws_janelas=wb["Janelas"]
        ws_ares=wb["Ares Condicionados"]
        wb_Casa_comodo=load_workbook("Casa_comodos.xlsx")
        ws=wb_Casa_comodo["Comodos"]
        
        for i,row in enumerate(ws.iter_rows(min_row=2), start=1):
            self.nomeComodos.append((f"{str(row[0].value)}",f"{str(row[1].value)}"))

        for i,row in enumerate(ws_lampadas.iter_rows(min_row=2), start=1):
            self.nomeLampadas.append((f"{str(row[0].value)}",f"{str(row[1].value)}","","",f"{str(row[4].value)}","","",f"{str(row[7].value)}"))


        for i,row in enumerate(ws_cortinas.iter_rows(min_row=2), start=1):
            self.nomeCortina.append((f"{str(row[0].value)}",f"{str(row[1].value)}","","",f"{str(row[4].value)}","","",""))


        for i,row in enumerate(ws_ares.iter_rows(min_row=2), start=1):
            if(row[2].value=="True"):
                self.nomeArCondicionado.append((f"{str(row[0].value)}",f"{str(row[1].value)}","Ligado",f"{str(row[3].value)}",f"{str(row[4].value)}","","",""))
            else:
                self.nomeArCondicionado.append((f"{str(row[0].value)}",f"{str(row[1].value)}","Desligado",f"{str(row[3].value)}",f"{str(row[4].value)}","","",""))

        for i,row in enumerate(ws_janelas.iter_rows(min_row=2), start=1):
            if(row[6].value=="True"):
                self.nomeJanelas.append((f"{str(row[0].value)}",f"{str(row[1].value)}","","","",f"{str(row[5].value)}","Trancado",""))
            else:
                self.nomeJanelas.append((f"{str(row[0].value)}",f"{str(row[1].value)}","","","",f"{str(row[5].value)}","Aberto",""))


    def CriarJanelas(self):
        self.comodoFrame = ComodoFrame(self)
        self.comodoFrame.pack(side= "top")
        self.labelDuplicata = customtkinter.CTkLabel(self.comodoFrame,
                                               text= "Já existe um comodo com esse nome, insira outro",
                                               text_color= "red")
        
        self.labelInexistente = customtkinter.CTkLabel(self.comodoFrame,
                                               text= "Esse cômodo não existe",
                                               text_color= "red")
        BotaoAdicionarComodo = BotaoAdd(self.comodoFrame, label="Adicionar novo cômodo")
        BotaoAdicionarComodo.configure(command= lambda:self.AdicionarComodoBotao())
        BotaoAdicionarComodo.pack(side = "bottom",pady= (10,10))
        
        BotaoRemoverComodo = BotaoRemove(self.comodoFrame, label="Remover cômodo")
        BotaoRemoverComodo.configure(command= lambda:self.RemoverComodoBotao())
        BotaoRemoverComodo.pack(side = "bottom",pady= (10,10))
        
        
        #Criando a pagina de cada comodo
        for nomes,numero in self.nomeComodos:
            contadorLampada = 0
            contadorArCondicionado = 0
            contadorJanela = 0
            contadorCortina = 0
            
            #Criando a pagina que exibe os tipos de dispositivos
            dispositivoFrame = DispositivosFrame(master = self, nome = nomes)
            self.dispositivosFrame[nomes] = dispositivoFrame
            dispositivoFrame.header.iconeBotao.configure(command = lambda: self.VoltarFrameComodos())
            
            #Criando a pagina das lampada e configurando os botoes que irão nela
            lampadaFrame = LampadasFrame(master=self)
            lampadaFrame.header.iconeBotao.configure(command = lambda n=nomes: self.VoltarFrameDispositivosLampadas(n))
            self.lampadasFrame[nomes] = lampadaFrame
            
            BotaoAdicionarLâmpada = BotaoAdd(self.lampadasFrame[nomes], label="Adicionar nova lâmpada")
            BotaoAdicionarLâmpada.pack(side = "bottom",pady= (10,10))
            
            for comodo,nome,ligado,temperatura,intensidade,abertura,tranca,cor in self.nomeLampadas:
                if comodo == nomes:
                    self.lampadasConfig[nome] = ConfigurarLampadas(master = self,
                                                    nome =nome,
                                                    intensidade=intensidade,
                                                    cor = cor
                                                    )
                    contadorLampada += 1
                    self.lampadasConfig[nome].header.iconeBotao.configure(command = lambda n=nomes: self.VoltarFrameLampadas(n))
                    
                    self.lampadasBotoes[nome] = BotaoLampada(self.lampadasFrame[nomes],
                                                             nomeLampada=nome,
                                                             cor=cor,
                                                             intensidade=intensidade)
                    self.lampadasBotoes[nome].configure(command = lambda n=nome:self.MudarFrameConfigLampadas(n))
                    self.lampadasBotoes[nome].pack(side="top", pady= (10,10))
            
            #Criando a pagina do ar condicionado e configurando os botoes que irão nela 
            arCondicionadoFrame = ArCondicionadoFrame(master=self)
            arCondicionadoFrame.header.iconeBotao.configure(command = lambda n=nomes: self.VoltarFrameDispositivosAr(n))
            self.ArCondicionadoFrame[nomes] = arCondicionadoFrame
            
            BotaoAdicionarAr = BotaoAdd(self.ArCondicionadoFrame[nomes], label="Adicionar novo ar")
            BotaoAdicionarAr.pack(side = "bottom",pady= (10,10))
             
            for comodo,nome,ligado,temperatura,intensidade,abertura,tranca,cor in self.nomeArCondicionado:
                if comodo == nomes:
                    self.arConfig[nome] = ConfigurarAr(master = self,
                                                    nome =nome,
                                                    intensidade=intensidade,
                                                    temperatura = temperatura,
                                                    ligado = ligado
                                                    )
                    self.arConfig[nome].header.iconeBotao.configure(command = lambda n=nomes: self.VoltarFrameAr(n))
                    contadorArCondicionado += 1
                    self.ArCondicionadoBotoes[nome] = BotaoArCondicionado(self.ArCondicionadoFrame[nomes],
                                                             nomeAr=nome,
                                                             ligado=ligado,
                                                             temperatura=temperatura,
                                                             intensidade=intensidade)
                    self.ArCondicionadoBotoes[nome].configure(command = lambda n=nome:self.MudarFrameConfigAr(n))
                    self.ArCondicionadoBotoes[nome].pack(side="top", pady= (10,10))
              
              
            #Criando a pagina das janelas e configurando os botoes que irão nela        
            janelaFrame = JanelaFrame(master=self)
            janelaFrame.header.iconeBotao.configure(command = lambda n=nomes: self.VoltarFrameDispositivosJanela(n))
            self.janelaFrame[nomes] = janelaFrame
            
            BotaoAdicionarJanela = BotaoAdd(self.janelaFrame[nomes], label="Adicionar nova janela")
            BotaoAdicionarJanela.pack(side = "bottom",pady= (10,10))
             
            for comodo,nome,ligado,temperatura,intensidade,abertura,tranca,cor in self.nomeJanelas:
                if comodo == nomes:
                    self.janelaConfig[nome] = ConfigurarJanela(master = self,
                                                    nome =nome,
                                                    abertura=abertura,
                                                    trancado = tranca
                                                    )
                    self.janelaConfig[nome].header.iconeBotao.configure(command = lambda n=nomes: self.VoltarFrameJanela(n))
                    contadorJanela += 1
                    self.janelaBotoes[nome] = BotaoJanela(self.janelaFrame[nomes],
                                                             nomeJanela=nome,
                                                             abertura=abertura,
                                                             trancado=tranca)
                    self.janelaBotoes[nome].configure(command = lambda n=nome:self.MudarFrameConfigJanela(n))
                    self.janelaBotoes[nome].pack(side="top", pady= (10,10))
             
             
            #Criando a pagina das cortinas e configurando os botoes que irão nela 
            cortinaFrame = CortinaFrame(master=self)
            cortinaFrame.header.iconeBotao.configure(command = lambda n=nomes: self.VoltarFrameDispositivosCortina(n))
            self.cortinasFrame[nomes] = cortinaFrame
            
            BotaoAdicionarCortina = BotaoAdd(self.cortinasFrame[nomes], label="Adicionar nova cortina")
            BotaoAdicionarCortina.pack(side = "bottom",pady= (10,10))
                    
            for comodo,nome,ligado,temperatura,intensidade,abertura,tranca,cor in self.nomeCortina:
                if comodo == nomes:
                    self.cortinaConfig[nome] = ConfigurarCortina(master = self,
                                                    nome =nome,
                                                    abertura=abertura,
                                                    )
                    self.cortinaConfig[nome].header.iconeBotao.configure(command = lambda n=nomes: self.VoltarFrameCortina(n))
                    contadorCortina += 1
                    self.cortinasBotoes[nome] = BotaoCortina(self.cortinasFrame[nomes],
                                                             nomeCortina=nome,
                                                             abertura=abertura)
                    self.cortinasBotoes[nome].configure(command = lambda n=nome:self.MudarFrameConfigCortina(n))
                    self.cortinasBotoes[nome].pack(side="top", pady= (10,10))        
                           
            
            #Criando os botões que irão na pagina dos dispositivos    
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
            
            #Colocando os botões da pagina do cômodo
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
        
    def MudarFrameConfigLampadas(self,nome):
        self.lampadasFrame[self.frameAtual].pack_forget()
        self.update()
        self.lampadasConfig[nome].pack(side ='top')
        self.lampadasConfig[nome].update()
        self.frameAtual = nome
        self.update()
        
    def VoltarFrameLampadas(self,nome):
        self.lampadasConfig[self.frameAtual].pack_forget()
        self.update()
        self.lampadasFrame[nome].pack(side='top')
        self.lampadasFrame[nome].update()
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
        
    def MudarFrameConfigAr(self,nome):
        self.ArCondicionadoFrame[self.frameAtual].pack_forget()
        self.update()
        self.arConfig[nome].pack(side ='top')
        self.arConfig[nome].update()
        self.frameAtual = nome
        self.update()
        
    def VoltarFrameAr(self,nome):
        self.arConfig[self.frameAtual].pack_forget()
        self.update()
        self.ArCondicionadoFrame[nome].pack(side='top')
        self.ArCondicionadoFrame[nome].update()
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
    
    def MudarFrameConfigJanela(self,nome):
        self.janelaFrame[self.frameAtual].pack_forget()
        self.update()
        self.janelaConfig[nome].pack(side ='top')
        self.janelaConfig[nome].update()
        self.frameAtual = nome
        self.update()
        
    def VoltarFrameJanela(self,nome):
        self.janelaConfig[self.frameAtual].pack_forget()
        self.update()
        self.janelaFrame[nome].pack(side='top')
        self.janelaFrame[nome].update()
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
        
    def MudarFrameConfigCortina(self,nome):
        self.cortinasFrame[self.frameAtual].pack_forget()
        self.update()
        self.cortinaConfig[nome].pack(side ='top')
        self.cortinaConfig[nome].update()
        self.frameAtual = nome
        self.update()
        
    def VoltarFrameCortina(self,nome):
        self.cortinaConfig[self.frameAtual].pack_forget()
        self.update()
        self.cortinasFrame[nome].pack(side='top')
        self.cortinasFrame[nome].update()
        self.update()
        self.frameAtual = nome      

        
    def AdicionarComodoBotao(self):
        self.inputComodoAdd = ComodoAddFrame(self.comodoFrame)
        self.inputComodoAdd.submit.configure(command = lambda:self.SubmeterAddComodo())
        self.inputComodoAdd.pack(side="bottom")
        
    def SubmeterAddComodo(self):
        NomeComodo = self.inputComodoAdd.input.get()
        self.labelDuplicata.pack_forget()
        for nomes,numero in self.nomeComodos:
            if nomes == NomeComodo:
                self.labelDuplicata.pack(side = "top")
                return
        
        self.casa.AdicionarComodo(NomeComodo)
        self.CarregarVetores()
        print(self.nomeComodos)
        
        
        #Criando o botao do novo comodo
        self.botoesComodo[NomeComodo] = BotaoComodo(self.comodoFrame, nomeComodo=NomeComodo, numeroDispositivos=0)
        self.botoesComodo[NomeComodo].configure(command = lambda n=NomeComodo:self.MudarFrameDispositivos(n))
        self.botoesComodo[NomeComodo].pack(side="top", pady= (10,10))

        #Criando o frame para os dispostivos do novo comodo        
        dispositivoFrame = DispositivosFrame(master = self, nome = NomeComodo)
        self.dispositivosFrame[NomeComodo] = dispositivoFrame
        dispositivoFrame.header.iconeBotao.configure(command = lambda: self.VoltarFrameComodos())
        
        #Criando os botões que irão na pagina dos dispositivos    
        self.botaoLampada = BotaoDispositivo(self.dispositivosFrame[NomeComodo], nomeComodo="Lâmpadas",
                                  numeroDispositivos= 0,
                                  caminho="src/icons/lampada.png")
        self.botaoLampada.configure(command = lambda n=NomeComodo:self.MudarFrameLampadas(n))
        self.botaoLampada.pack(side="top", pady= (10,10))
        lampadaFrame = LampadasFrame(master=self)
        lampadaFrame.header.iconeBotao.configure(command = lambda n=NomeComodo: self.VoltarFrameDispositivosLampadas(n))
        self.lampadasFrame[NomeComodo] = lampadaFrame
        
        BotaoAdicionarLâmpada = BotaoAdd(self.lampadasFrame[NomeComodo], label="Adicionar nova lâmpada")
        BotaoAdicionarLâmpada.pack(side = "bottom",pady= (10,10))
        
            
        self.botaoAr = BotaoDispositivo(self.dispositivosFrame[NomeComodo], nomeComodo="Ar Condicionado",
                                  numeroDispositivos= 0,
                                  caminho="src/icons/arCondicionado.png")
        self.botaoAr.configure(command = lambda n=NomeComodo:self.MudarFrameAr(n))
        self.botaoAr.pack(side="top", pady= (10,10))
        arCondicionadoFrame = ArCondicionadoFrame(master=self)
        arCondicionadoFrame.header.iconeBotao.configure(command = lambda n=NomeComodo: self.VoltarFrameDispositivosAr(n))
        self.ArCondicionadoFrame[NomeComodo] = arCondicionadoFrame
        BotaoAdicionarAr = BotaoAdd(self.ArCondicionadoFrame[NomeComodo], label="Adicionar novo ar")
        BotaoAdicionarAr.pack(side = "bottom",pady= (10,10))
        
        self.botaoJanela = BotaoDispositivo(self.dispositivosFrame[NomeComodo], nomeComodo="Janela",
                                  numeroDispositivos= 0,
                                  caminho="src/icons/Janela.png")
        self.botaoJanela.configure(command = lambda n=NomeComodo:self.MudarFrameJanela(n))
        self.botaoJanela.pack(side="top", pady= (10,10))
        janelaFrame = JanelaFrame(master=self)
        janelaFrame.header.iconeBotao.configure(command = lambda n=NomeComodo: self.VoltarFrameDispositivosJanela(n))
        self.janelaFrame[NomeComodo] = janelaFrame
        BotaoAdicionarJanela = BotaoAdd(self.janelaFrame[NomeComodo], label="Adicionar nova janela")
        BotaoAdicionarJanela.pack(side = "bottom",pady= (10,10))
        
        
        self.botaoCortina = BotaoDispositivo(self.dispositivosFrame[NomeComodo], nomeComodo="Cortina",
                                  numeroDispositivos= 0,
                                  caminho="src/icons/cortina.png")
        self.botaoCortina.configure(command = lambda n=NomeComodo:self.MudarFrameCortina(n))
        self.botaoCortina.pack(side="top", pady= (10,10))  
        cortinaFrame = CortinaFrame(master=self)
        cortinaFrame.header.iconeBotao.configure(command = lambda n=NomeComodo: self.VoltarFrameDispositivosCortina(n))
        self.cortinasFrame[NomeComodo] = cortinaFrame 
        BotaoAdicionarCortina = BotaoAdd(self.cortinasFrame[NomeComodo], label="Adicionar nova cortina")
        BotaoAdicionarCortina.pack(side = "bottom",pady= (10,10))   
        
        self.inputComodoAdd.pack_forget()
        
    def RemoverComodoBotao(self):
        self.inputComodoRemove = ComodoRemoveFrame(self.comodoFrame)
        self.inputComodoRemove.submit.configure(command = lambda:self.SubmeterRemoverComodo())
        self.inputComodoRemove.pack(side="top")
        
    def SubmeterRemoverComodo(self):
        NomeComodo = self.inputComodoRemove.input.get()
        self.CarregarVetores()
        print(self.nomeComodos)
        self.labelInexistente.pack_forget()
        for nomes,numero in self.nomeComodos:
            if nomes == NomeComodo:
                self.casa.RemoverComodo(NomeComodo)
                self.CarregarVetores()
                self.inputComodoRemove.pack_forget()
                self.botoesComodo[NomeComodo].pack_forget()
                self.botoesComodo[NomeComodo].destroy()
                
                #Destruindo o frame para os dispostivos do novo comodo        
                self.dispositivosFrame[NomeComodo].destroy()
                self.lampadasFrame[NomeComodo].destroy()
                self.ArCondicionadoFrame[NomeComodo].destroy()
                self.janelaFrame[NomeComodo].destroy()
                self.cortinasFrame[NomeComodo].destroy()
                return
        self.inputComodoRemove.pack_forget()
        self.labelInexistente.pack(side="top")
        self.inputComodoRemove.pack(side = "top")
app = App()
app.mainloop()