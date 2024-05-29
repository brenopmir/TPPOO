import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

from Interfaces.Interfaces_dispositivo import  InterfaceDispositivo
from abc import ABC,abstractmethod

class Dispositivo(InterfaceDispositivo,ABC):
    def __init__(self,nome:str)->None:
        self.__nome=nome

    def Nome(self) -> str:
        return self.__nome
    
    def SetNome(self, nomenovo: str) -> None:
        self.__nome=nomenovo

    #Precisamos Implementar Ainda
    #@abstractmethod     
    def SalvarDispositivo(self, nomearquivo: str) -> None:
        print("Precisamos implementar ainda ")
