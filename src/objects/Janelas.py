import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

from Interfaces.Interfaces_janelas import InterfaceJanela
from Dispositivo import Dispositivo
from openpyxl import Workbook,load_workbook
from typing import Type

wb=load_workbook("Casa.xlsx")
ws=wb.active
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
    
    def SalvarDispositivo(self) -> None:
        #O True não aparece no arquivo excel|True bonitinho então eu fiz esse if para ficar legivel 
        if(self.__tranca==True):
            ws.append([f"{self.Nome()}",'Janela',None,None,None,self.__abertura,'True',None])
        else:
             ws.append([f"{self.Nome()}",'Janela',None,None,None,self.__abertura,'False',None])
        wb.save("Casa.xlsx")


def criar_instancia_janela(classe:Type[Janela],nome:str,abertura:int,tranca:bool,)->Janela:
    instancia=classe(nome,abertura,tranca)
    return instancia