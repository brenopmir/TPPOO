import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

from Interfaces.Interfaces_lampadas import InterfaceLampadas
from Dispositivo import Dispositivo

class Lampadas(Dispositivo,InterfaceLampadas):
    def __init__(self, nome: str,cor:str,intensidade:int) -> None:
        super().__init__(nome)
        self.__cor=cor
        self.__intensidade=intensidade
    
    def Cor(self) -> str:
        return self.__cor
    
    def SetCor(self, cornova: str) -> None:
        self.__cor=cornova

    def Intensidade(self) -> int:
        return self.__intensidade
    
    def SetIntensidade(self, intensidadenova: int) -> None:
        self.__intensidade=intensidadenova