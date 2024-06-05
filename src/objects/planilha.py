# esse arquivo tem como função criar a planilha inicial 
from openpyxl import Workbook

def iniciar_planilhas():
    wb=Workbook()
    ws=wb.active

    ws.title="Comodo"

    wb.create_sheet("Lampadas")
    wb.create_sheet("Ares Condicionados")
    wb.create_sheet("Janelas")
    wb.create_sheet("Cortinas")

    ws=wb["Lampadas"]
    ws.append(["Comodo","Nome","Ligado","Temperatura","Intensidade","Abertura","Tranca","Cor"])

    ws=wb["Ares Condicionados"]
    ws.append(["Comodo","Nome","Ligado","Temperatura","Intensidade","Abertura","Tranca","Cor"])

    ws=wb["Janelas"]
    ws.append(["Comodo","Nome","Ligado","Temperatura","Intensidade","Abertura","Tranca","Cor"])

    ws=wb["Cortinas"]
    ws.append(["Comodo","Nome","Ligado","Temperatura","Intensidade","Abertura","Tranca","Cor"])

    wb.save("Casa.xlsx")


    wb_Casa_comodo=Workbook()
    ws=wb_Casa_comodo.active

    ws.title="Comodos"
    ws.append(["Comodo","Numero Dispositivos"])
    wb_Casa_comodo.save("Casa_comodos.xlsx")

