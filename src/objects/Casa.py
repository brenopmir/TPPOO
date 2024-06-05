import sys
import os

# Pega o diretório pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# fornece o caminho
sys.path.append(diretorioPai)

from openpyxl import Workbook,load_workbook
from Interfaces.Interfaces_casa import InterfaceCasa
from Comodo import Comodo, criar_comodo

wb_Casa_comodo=load_workbook("Casa_comodos.xlsx")
ws=wb_Casa_comodo["Comodos"]

class Casa(InterfaceCasa):
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.comodos = {}

    def Nome(self) -> str:
        return self.__nome
    
    def SetNome(self, nomenovo: str) -> None:
        self.__nome = nomenovo

    def AdicionarComodo(self, nomedocomodo: str) -> None:
        if not self.VerificarDuplicado(nomedocomodo):
            self.comodos[nomedocomodo] = criar_comodo(Comodo, nomedocomodo)
            ws.append([nomedocomodo,0])
            wb_Casa_comodo.save("Casa_comodos.xlsx")  # Salva o workbook após adicionar o cômodo
        else:
            return
    
    def RemoverComodo(self, nomecomodo: str) -> None:
        if nomecomodo in self.comodos:
                self.comodos.pop(nomecomodo)
        for i, row in enumerate(ws.iter_rows(), start=1):
                if row[0].value == nomecomodo:
                    ws.delete_rows(i, 1)
                     
        wb_Casa_comodo.save("Casa_comodos.xlsx") # Salva o workbook após remover o cômodo

    def VerificarDuplicado(self, nomedocomodo: str) -> bool:
        for row in ws.iter_rows(values_only=True):
            if nomedocomodo in row:
                return True
        return False

    def Salvar_Quantidadede_dispositivos_Comodo(self) -> None:
      for row in range(2,(ws.max_row+1)):
        ws['B'+str(row)]=self.comodos[ws['A' + str(row)].value].Quantidade_dispositivo()
        wb_Casa_comodo.save("Casa_comodos.xlsx")







"""
testeCasa=Casa("Breno")
testeCasa.AdicionarComodo("Quarto")
testeCasa.comodos["Quarto"].AdicionarDispositivo(1,"lampada") 
testeCasa.comodos["Quarto"].AdicionarDispositivo(2,"cortina") 
testeCasa.comodos["Quarto"].AdicionarDispositivo(3,"arcondicionado")

testeCasa.AdicionarComodo("Cozinha")
testeCasa.comodos["Cozinha"].AdicionarDispositivo(1,"lampada1") 
testeCasa.comodos["Cozinha"].AdicionarDispositivo(2,"cortina1") 
testeCasa.comodos["Cozinha"].AdicionarDispositivo(3,"arcondicionado1")
#testeCasa.comodos["Quarto"].ConfigurarLampada("lampada","vermelho",100,"testetrocar")
#testeCasa.comodos["Quarto"].ConfigurarLampada("testetrocar","roxo",70,"Breno")
#testeCasa.Salvar_Quantidadede_dispositivos_Comodo()
#testeCasa.RemoverComodo("Quarto")
#testeCasa.comodos["Quarto"].RemoverDispositivo(1,"lampada")
#testeCasa.comodos["Quarto"].RemoverDispositivo(2,"cortina") 
#testeCasa.comodos["Quarto"].RemoverDispositivo(3,"arcondicionado")
#testeCasa.Salvar_Quantidadede_dispositivos_Comodo()
testeCasa.Salvar_Quantidadede_dispositivos_Comodo()
"""

