import pandas as pd
import openpyxl

archivo_data = pd.read_csv('vulneibilidades.csv')

tabla_orden = archivo_data.pivot_table(index='IP Address', columns='Name', values='OS', aggfunc='order')
print(tabla_orden)