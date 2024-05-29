import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

from Interfaces.Interfaces_arcondicionado import InterfaceAr_Condicionado
from Dispositivo import Dispositivo

class Ar_Condicionado(Dispositivo,InterfaceAr_Condicionado):
    def __init__(self, nome: str,ligado:bool,temperatura:int,intensidade:int) -> None:
        super().__init__(nome)
        self.__ligado=ligado
        self.__temperatura=temperatura
        self.__intensidade=intensidade 
    
    def Ligado(self) -> bool:
        return self.__ligado
    
    def SetLigado(self, ligarnovo: bool) -> None:
        self.__ligado=ligarnovo
    
    def Temperatura(self) -> int:
        return self.__temperatura
    
    def SetTemperatura(self, temperaturanova: int) -> None:
        self.__temperatura=temperaturanova
    
    def Intensidade(self) -> int:
        return self.__intensidade
    
    def SetIntensidade(self, intensidadenova: int) -> None:
        self.__intensidade=intensidadenova