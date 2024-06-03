import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)

from Interfaces.Interfaces_casa import InterfaceCasa
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from Comodo import Comodo,criar_comodo

wb=load_workbook("Casa.xlsx")
ws=wb.active

#Todos_comodos=[]
class Casa(InterfaceCasa):
    def __init__(self,nome:str) -> None:
        self.__nome=nome
        self.__comodos={}

    def Nome(self) -> str:
        return self.__nome
    
    def SetNome(self, nomenovo: str) -> None:
        self.__nome=nomenovo

    def AdicionarComodo(self, nomedocomodo: str) -> None:
        if(self.VerificarDuplicado(nomedocomodo)==False):
            self.__comodos[nomedocomodo] = criar_comodo(Comodo,nomedocomodo)
        else:
            return
    
    def RemoverComodo(self, nomecomodo: str) -> None:
        i=0
        for j in self.__comodos: # primeiro loop possui a função de apagar o nome do comodo a ser removido do dict 
            if(j==nomecomodo):
                self.__comodos.pop(j)
                break
        for row in ws.iter_rows():# segundo loop tem a função de apagar o comodo do arquivo excel 
            if(row[0].value==nomecomodo):
                ws.delete_rows((i+1),1)
                break
            i+=1
            wb.save("Casa.xlsx")
        else:
            return
        
    def ListarComodos(self)->list[str]:
         return list(self.__comodos.keys())
        
    def VerificarDuplicado(self, nomedocomodo: str) -> bool:
        for row in ws.iter_rows(values_only=True):
            if nomedocomodo in row:
                return True
        return False

    def SalvarComodo(self) -> None:
        for i in self.__comodos:
            ws.append([i,self.__comodos[i]. Quantidade_dispositivo()])
        wb.save("Casa.xlsx")

        

        