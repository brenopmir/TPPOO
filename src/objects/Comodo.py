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

class Comodo(InterfaceComodo):
    def __init__(self,nome:str) -> None:
        self.__nome=nome
        self.__quantidade_dispositivo=0
        self.__lampadas={}
        self.__arescondicionados={}
        self.__cortinas={}
        self.__janelas={}
        self.__numerodispositivos=0
    
    def Nome(self) -> str:
        return self.__nome
    
    def SetNome(self, nomenovo: str) -> None:
        self.__nome=nomenovo
    
    def Quantidade_dispositivo(self)->int:
         return self.__quantidade_dispositivo
    
    def AdicionarDispositivo(self, tipo: int, nome: str) -> None:
         print("algo")
    
    def ConfigurarTodos(self, tipo: int, nome: str) -> None:
         print("algo")
    
    def ListarDispositivos(self) -> None:
         print("algo")
    
    def RemoverDispositivo(self, tipo: int, nome: str) -> None:
         print("algo")
    
def criar_comodo(classe:Type[Comodo],nome:str)->Comodo:
     instancia=classe(nome)
     return instancia
     