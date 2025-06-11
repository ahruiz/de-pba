# codigo para mostrar datos en tablas

from tabulate import tabulate
from datetime import datetime

# Crear una lista de listas
data = [['1000', 0, 0, datetime.now(), 0]]
columnas =["SALDO", "RETIRO", "NUEVO SALDO", "FECHA", "FOLIO"]

# Mostrar la tabla
print(tabulate(data, headers=columnas, tablefmt='grid'))

# Mostrar la tabla en formato HTML
#html_table = tabulate(data, headers=columns, tablefmt='html')
#print(html_table)

