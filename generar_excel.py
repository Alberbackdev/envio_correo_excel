from openpyxl import Workbook

book = Workbook()
sheet = book.active


columnas= ['A', 'B', 'C']
contador=2
for i in columnas:
    print(i)
    sheet[f'{i}{contador}'] = i

book.save('prueba.xlsx')