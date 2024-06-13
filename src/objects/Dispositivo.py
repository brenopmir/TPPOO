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

    #Retorna o Nome do dispositivo
    def Nome(self) -> str:
        return self.__nome
    
    #Seta o nome do dispositivo
    def SetNome(self, nomenovo: str) -> None:
        self.__nome=nomenovo
