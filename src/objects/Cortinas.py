import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

from Interfaces.Interfaces_cortinas import InterfaceCortinas
from objects.Dispositivo import Dispositivo
from typing import Type

class Cortina(InterfaceCortinas,Dispositivo):
    def __init__(self, nome: str,intensidade:int) -> None:
        super().__init__(nome)
        self.__intensidade=intensidade

    #Retorna a propriedade Intensidade da Cortina
    def Intensidade(self) -> int:
        return self.__intensidade
    
    #Seta a propriedade Intensidade da Cortina
    def SetIntensidade(self, intensidadenova: int) -> None:
        self.__intensidade=intensidadenova

#Cria uma instancia da Cortina com todas as suas propriedades 
def criar_instancia_cortina(classe:Type[Cortina],nome:str,intensidade:int)->Cortina:
    instancia=classe(nome,intensidade)
    return instancia