import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

from Interfaces.Interfaces_cortinas import InterfaceCortinas
from Dispositivo import Dispositivo

class Cortina(InterfaceCortinas,Dispositivo):
    def __init__(self, nome: str,intensidade:int) -> None:
        super().__init__(nome)
        self.__intensidade=intensidade

    def Intensidade(self) -> int:
        return self.__intensidade
    
    def SetIntensidade(self, intensidadenova: int) -> None:
        self.__intensidade=intensidadenova