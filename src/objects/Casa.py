import sys
import os

# Pega o diretório pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# fornece o caminho
sys.path.append(diretorioPai)

from openpyxl import Workbook,load_workbook
from Interfaces.Interfaces_casa import InterfaceCasa
from Comodo import Comodo, criar_comodo

wb=Workbook()
ws=wb.active

ws.title="Comodos"
ws.append(["Comodo","Numero Dispositivos"])

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
            wb.save("Casa_comodos.xlsx")  # Salva o workbook após adicionar o cômodo
        else:
            return
    
    def RemoverComodo(self, nomecomodo: str) -> None:
        if nomecomodo in self.comodos:
            self.comodos.pop(nomecomodo)
            for i, row in enumerate(ws.iter_rows(), start=1):
                if row[0].value == nomecomodo:
                    ws.delete_rows(i, 1)
                    wb.save("Casa_comodos.xlsx")  # Salva o workbook após remover o cômodo
                    break
    
    def ListarComodos(self) -> list[str]:
        listacomodos = []
        for row in range(2, ws.max_row + 1):
            listacomodos.append(ws['A' + str(row)].value)
        return listacomodos
        
    def VerificarDuplicado(self, nomedocomodo: str) -> bool:
        for row in ws.iter_rows(values_only=True):
            if nomedocomodo in row:
                return True
        return False

    def Salvar_Quantidadede_dispositivos_Comodo(self) -> None:
      for row in range(2,(ws.max_row+1)):
        ws['B'+str(row)]=self.comodos[ws['A' + str(row)].value].Quantidade_dispositivo()
        wb.save("Casa_comodos.xlsx")
