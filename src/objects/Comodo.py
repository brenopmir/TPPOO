import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)


from Interfaces.Interfaces_arcondicionado import InterfaceAr_Condicionado
from Interfaces.Interfaces_comodo import InterfaceComodo
from Interfaces.Interfaces_cortinas import InterfaceCortinas
from Interfaces.Interfaces_dispositivo import InterfaceDispositivo
from Interfaces.Interfaces_janelas import InterfaceJanela
from Interfaces.Interfaces_lampadas import InterfaceLampadas
from ArCondicionado import Ar_Condicionado,criar_instancia_ar_condicionado
from Cortinas import Cortina,criar_instancia_cortina
from Janelas import Janela,criar_instancia_janela
from Lampadas import Lampadas,criar_instancia_lampada
from Dispositivo import Dispositivo
from typing import Type
from openpyxl import Workbook,load_workbook

wb=load_workbook("Casa.xlsx")
ws=wb.active
ws_lampadas=wb["Lampadas"]
ws_cortinas=wb["Cortinas"]
ws_janelas=wb["Janelas"]
ws_ares=wb["Ares Condicionados"]
class Comodo(InterfaceComodo):
    def __init__(self,nome:str) -> None:
        self.__nome=nome
        self.__quantidade_dispositivo=0
        self.__lampadas={}
        self.__arescondicionados={}
        self.__cortinas={}
        self.__janelas={}
    
    def Nome(self) -> str:
        return self.__nome
    
    def SetNome(self, nomenovo: str) -> None:
        self.__nome=nomenovo
    
    def Quantidade_dispositivo(self)->int:
         return self.__quantidade_dispositivo
    
    # Cria um  dispositivo de um tipo, sendo Lampada,Cortina,Arcondicionado e  Janela, 1,2,3 e 4  respectivamente e com o nome que o usuario escolher
    def AdicionarDispositivo(self, tipo: int, nome: str) -> None:
          if(tipo==1):
               self.__lampadas[nome]=criar_instancia_lampada(Lampadas,nome,None,0)
               self.__quantidade_dispositivo+=1
               ws_lampadas.append([self.__nome,f"{self.__lampadas[nome].Nome()}", None,None,self.__lampadas[nome].Intensidade(),None,None,self.__lampadas[nome].Cor()])
          
          elif(tipo==2):
               self.__cortinas[nome]=criar_instancia_cortina(Cortina,nome,0)
               self.__quantidade_dispositivo+=1
               ws_cortinas.append([self.__nome,f"{self.__cortinas[nome].Nome()}", None,None,self.__cortinas[nome].Intensidade(),None,None,None])
          
          elif(tipo==3):
               self.__arescondicionados[nome]=criar_instancia_ar_condicionado(Ar_Condicionado,nome,False,0,0)
               self.__quantidade_dispositivo+=1
               if(self.__arescondicionados[nome].Ligado()==True):
                    ws_ares.append([self.__nome,f"{self.__arescondicionados[nome].Nome()}","True",self.__arescondicionados[nome].Temperatura(),self.__arescondicionados[nome].Intensidade(),None,None,None])
               else:
                    ws_ares.append([self.__nome,f"{self.__arescondicionados[nome].Nome()}","False",self.__arescondicionados[nome].Temperatura(),self.__arescondicionados[nome].Intensidade(),None,None,None])
          
          elif(tipo==4):
               self.__janelas[nome]=criar_instancia_janela(Janela,nome,0,False)
               self.__quantidade_dispositivo+=1
               if(self.__janelas[nome].Tranca()==True):
                    ws_janelas.append([self.__nome,f"{self.__janelas[nome].Nome()}",None,None,None,self.__janelas[nome].Abertura(),"True",None])
               else:
                    ws_janelas.append([self.__nome,f"{self.__janelas[nome].Nome()}",None,None,None,self.__janelas[nome].Abertura(),"False",None])
          wb.save("Casa.xlsx")
    
     # remove o dispositivo de um tipo,sendo Lampada,Cortina,Arcondicionado e  Janela, 1,2,3 e 4  respectivamente, que possui determinado nome      
    def RemoverDispositivo(self, tipo:str, nome: str) -> None:
          if(tipo==1):
                    if nome in self.__lampadas:
                         self.__lampadas.pop(nome)
                    for i, row in enumerate(ws_lampadas.iter_rows(), start=1):
                         if row[0].value == self.Nome() and row[1].value == nome :
                              ws_lampadas.delete_rows(i, 1)
                                                
          elif(tipo==2):
                    if nome in self.__cortinas:
                         self.__cortinas.pop(nome)
                    for i, row in enumerate(ws_cortinas.iter_rows(), start=1):
                         if row[0].value == self.Nome() and row[1].value == nome :
                              ws_cortinas.delete_rows(i, 1)                              
          elif(tipo==3):
                    if nome in self.__arescondicionados:
                         self.__arescondicionados.pop(nome)
                    for i, row in enumerate(ws_ares.iter_rows(), start=1):
                         if row[0].value == self.Nome() and row[1].value == nome :
                              ws_ares.delete_rows(i, 1)
                                                            
          elif(tipo==4):
                    if nome in self.__janelas:
                         self.__janelas.pop(nome)
                    for i, row in enumerate(ws_janelas.iter_rows(), start=1):
                         if row[0].value == self.Nome() and row[1].value == nome :
                              ws_janelas.delete_rows(i, 1)
                               
          wb.save("Casa.xlsx")

   # def VerificarDuplicado(self,tipodispositivo:int,nomedodispositivo: str) -> bool:
          #pass
    
    def ConfigurarTodos(self, tipo: int, nome: str) -> None:
         print("algo")
     
    
def criar_comodo(classe:Type[Comodo],nome:str)->Comodo:
     instancia=classe(nome)
     return instancia

"""
testeComodo=Comodo("Quarto")
testeComodo.AdicionarDispositivo(1,"lampada")  
testeComodo.AdicionarDispositivo(2,"cortina")  
testeComodo.AdicionarDispositivo(3,"ar")  
testeComodo.AdicionarDispositivo(4,"janela")
testeComodo.RemoverDispositivo(1,"lampada")
testeComodo.RemoverDispositivo(2,"cortina")
testeComodo.RemoverDispositivo(3,"ar")  
testeComodo.RemoverDispositivo(4,"janela")
"""
