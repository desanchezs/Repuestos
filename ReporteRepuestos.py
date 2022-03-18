import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from Reporte import Reporte
# Lectura de los dos DataFrames
pd.set_option('display.max_columns', None)
path = dname
df2019 = pd.read_excel(path + '\Repuestos2019.xlsx')
df2020 = pd.read_excel(path + '\Repuestos2020.xlsx')
df2019 = df2019.drop('DESCRIPCION CUENTA', 1)

# Union de los dos DataFrames
df = pd.concat([df2019, df2020], ignore_index=True)

df['FECHA DE CIERRE'] = pd.to_datetime(df['FECHA DE CIERRE'])

# Creacion de las columnas de Kilometraje y
df.insert(loc=4, column='KILOMETRAJE', value=list(df['DESCRIPCION'].str.findall('\(([^)]+)').apply(', '.join).str.replace("KMS=", "").str.split(",")))
df.insert(loc=5, column='LEN_KMTRAJE', value=[len(x) for x in df['KILOMETRAJE']])
partial = df.DESCRIPCION.str.findall(r'[^,;\s]+')
df.insert(loc=4, column='PARTE_AFECTADA', value=[pos[0] for pos in list(partial)])
#print(df.head())
#%%
# Limpieza de 'PARTE_AFECTADA'
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('HABITACULO.', 'HABITACULO')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('PUERTASSE', 'PUERTAS')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('LUBRICACIÓN', 'LUBRICACION')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('VELOCIMETRO_x000D_RT(4870):VELOCIMETRO', 'VELOCIMETRO')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('HABITACULOINSTALAR', 'HABITACULO')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('ESPEJOS.', 'ESPEJOS')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('LUCES.', 'LUCES')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('VIDRIOS.', 'VIDRIOS')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('PUERTAS.', 'PUERTAS')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('CORREAS.', 'CORREAS.')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('LLANTAS.', 'LLANTAS')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('PISO.', 'PISO.')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('DESEMPAÑADORES', 'DESEMPANADORES')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('TELEMATICA_x000D_', 'TELEMATICA')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('HABITACULO_x000D_', 'HABITACULO')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('SUSPENSION_x000D_', 'SUSPENSION')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('FRENOS-', 'FRENOS')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('LLANTAS_x000D_', 'LLANTAS')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('LUBRICACIÓN_x000D_', 'LUBRICACION')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('LUCES_x000D_', 'LUCES')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('ESPEJOS_x000D_', 'ESPEJOS')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('ARTICULACION_x000D_', 'ARTICULACION')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('PUERTAS_x000D_', 'PUERTAS')
df['PARTE_AFECTADA'] = df['PARTE_AFECTADA'].replace('DIFERENCIAL_x000D_', 'DIFERENCIAL')

reporte = Reporte(df)

