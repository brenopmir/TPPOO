# esse arquivo tem como função criar a planilha inicial 
from openpyxl import Workbook

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
