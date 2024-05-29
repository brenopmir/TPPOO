import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

from Interfaces.Interfaces_janelas import InterfaceJanela
from Dispositivo import Dispositivo

class Janela(Dispositivo,InterfaceJanela):
    def __init__(self, nome: str,abertura:int,tranca:bool) -> None:
        super().__init__(nome)
        self.__abertura=abertura
        self.__tranca=tranca
    
    def Abertura(self) -> int:
        return self.__abertura
    
    def SetAbertura(self, aberturanova: int) -> None:
        self.__abertura=aberturanova
    
    def Tranca(self) -> bool:
        return self.__tranca
    
    def SetTranca(self, trancanova: bool) -> None:
        self.__tranca=trancanova