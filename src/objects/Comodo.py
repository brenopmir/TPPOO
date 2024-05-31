import sys
import os

# Pega o diretorio pai do arquivo
diretorioPai = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#fornece o caminho
sys.path.append(diretorioPai)


from Interfaces.Interfaces_arcondicionado import InterfaceAr_Condicionado
from Interfaces.Interfaces_comodo import InterfaceComodo
from Interfaces.Interfaces_cortinas import InterfaceCortinas
from Interfaces.Interfaces_dispositivo import InterfaceDispositivo
from Interfaces.Interfaces_janelas import InterfaceJanela
from Interfaces.Interfaces_lampadas import InterfaceLampadas
from ArCondicionado import Ar_Condicionado,criar_instancia_ar_condicionado
from Cortinas import Cortina,criar_instancia_cortina
from Janelas import Janela,criar_instancia_janela
from Lampadas import Lampadas,criar_instancia_lampada
from Dispositivo import Dispositivo
from typing import Type
from openpyxl import Workbook,load_workbook

class Comodo(InterfaceComodo):
    pass