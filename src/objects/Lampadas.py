import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

from Interfaces.Interfaces_lampadas import InterfaceLampadas
from objects.Dispositivo import Dispositivo
from typing import Type
class Lampadas(Dispositivo,InterfaceLampadas):
    def __init__(self, nome: str,cor:str,intensidade:int) -> None:
        super().__init__(nome)
        self.__cor=cor
        self.__intensidade=intensidade

    #Retorna a cor da Lampada 
    def Cor(self) -> str:
        return self.__cor
     
    #Seta a cor da Lampada
    def SetCor(self, cornova: str) -> None:
        self.__cor=cornova

    #Retorna a Intensidade da luminosidade da Lampada
    def Intensidade(self) -> int:
        return self.__intensidade
    
    #Seta a intensidade da Lampada
    def SetIntensidade(self, intensidadenova: int) -> None:
        self.__intensidade=intensidadenova

#Cria uma instancia da Lampada com todas as suas propriedades 
def criar_instancia_lampada(classe:Type[Lampadas],nome:str,cor:str,intensidade:int)->Lampadas:
    instancia=classe(nome,cor,intensidade)
    return instancia