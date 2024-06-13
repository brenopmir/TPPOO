import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

from Interfaces.Interfaces_arcondicionado import InterfaceAr_Condicionado
from Dispositivo import Dispositivo
from typing import Type

class Ar_Condicionado(Dispositivo,InterfaceAr_Condicionado):
    def __init__(self, nome: str,ligado:bool,temperatura:int,intensidade:int) -> None:
        super().__init__(nome)
        self.__ligado=ligado
        self.__temperatura=temperatura
        self.__intensidade=intensidade 
    
    #Retorna se o Ar Condicionado está ligado ou não, retornando True se estiver e False se não
    def Ligado(self) -> bool:
        return self.__ligado
    
    #Seta a propriedade se está ligado no Ar Condicionado
    def SetLigado(self, ligarnovo: bool) -> None:
        self.__ligado=ligarnovo
    
    #Retorna a Temperatura que o Ar Condicionado está emitindo
    def Temperatura(self) -> int:
        return self.__temperatura
    
    #Seta a propriedade Temperatura do Ar Condicionado
    def SetTemperatura(self, temperaturanova: int) -> None:
        self.__temperatura=temperaturanova
    
    #Retorna a propriedade Intensidade do Ar Condicionado
    def Intensidade(self) -> int:
        return self.__intensidade
    
    #Seta a propriedade Intensidade do Ar Condicionado
    def SetIntensidade(self, intensidadenova: int) -> None:
        self.__intensidade=intensidadenova

#Cria uma instancia do Ar Condicionado com todas as suas propriedades 
def criar_instancia_ar_condicionado(classe:Type[Ar_Condicionado],nome:str,ligado:bool,temperatura:int,intensidade:int)->Ar_Condicionado:
    instancia=classe(nome,ligado,temperatura,intensidade)
    return instancia