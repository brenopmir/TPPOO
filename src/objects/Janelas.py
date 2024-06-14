import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

from Interfaces.Interfaces_janelas import InterfaceJanela
from objects.Dispositivo import Dispositivo
from typing import Type

class Janela(Dispositivo,InterfaceJanela):
    def __init__(self, nome: str,abertura:int,tranca:bool) -> None:
        super().__init__(nome)
        self.__abertura=abertura
        self.__tranca=tranca
    
     #Retorna a abertura da Janela
    def Abertura(self) -> int:
        return self.__abertura
    
    #Seta a abertura da Janela 
    def SetAbertura(self, aberturanova: int) -> None:
        self.__abertura=aberturanova
    
    #Retorna se a Janela está Trancada ou não
    def Tranca(self) -> bool:
        return self.__tranca
    
    #Seta a propriedade Trancar da Janela 
    def SetTranca(self, trancanova: bool) -> None:
        self.__tranca=trancanova

#Cria uma instancia da Janela com todas as suas propriedades    
def criar_instancia_janela(classe:Type[Janela],nome:str,abertura:int,tranca:bool,)->Janela:
    instancia=classe(nome,abertura,tranca)
    return instancia