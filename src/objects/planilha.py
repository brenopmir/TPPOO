# esse arquivo tem como função criar a planilha inicial 
from openpyxl import Workbook

wb=Workbook()
ws=wb.active

ws.title="Casa"

ws.append(["Nome","Tipo","Ligado","Temperatura","Intensidade","Abertura","Tranca","Cor"])

wb.save("Casa.xlsx")
