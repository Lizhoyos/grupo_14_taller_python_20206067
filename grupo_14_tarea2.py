# -*- coding: utf-8 -*-
"""GRUPO_14_Tarea2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MWVY-Pn8ZZFi-YZqZGYMZAj5cazdaTOy

**Tarea grupal 2**
"""



"""1. Copia el siguiente diccionario en una cédula de Colab. A partir de él, crea un dataframe llamado 𝒏𝒇𝒐 utilizando Pandas.


***data_ciudades*** = {
′𝑪𝒊𝒖𝒅𝒂𝒅′: [′𝑳𝒊𝒎𝒂′, ′𝑨𝒓𝒆𝒒𝒖𝒊𝒑𝒂′, ′𝑻𝒓𝒖𝒋𝒊𝒍𝒍𝒐′, ′𝑪𝒖𝒔𝒄𝒐′, ′𝑪𝒉𝒊𝒄𝒍𝒂𝒚𝒐′, ′𝑷𝒊𝒖𝒓𝒂′, ′𝑰𝒒𝒖𝒊𝒕𝒐𝒔′, ′𝑯𝒖𝒂𝒏𝒄𝒂𝒚𝒐′, ′𝑻𝒂𝒄𝒏𝒂′, ′𝑷𝒖𝒄𝒂𝒍𝒍
′𝑯𝒂𝒃𝒊𝒕𝒂𝒏𝒕𝒆𝒔′: [𝟏𝟎𝟒𝟕𝟗𝟗𝟔, 𝟏𝟎𝟎𝟏𝟔𝟗, 𝟗𝟐𝟑𝟑𝟏, 𝟒𝟐𝟖𝟒𝟓𝟎, 𝟑𝟎𝟓𝟕𝟏𝟕, 𝟒𝟖𝟒𝟒𝟕𝟓, 𝟒𝟒𝟏𝟔𝟒𝟗, 𝟑𝟖𝟓𝟎𝟗𝟖, 𝟐𝟗𝟒𝟑𝟗𝟓, 𝟐𝟖𝟑𝟕𝟑𝟒],
′𝑨𝒓𝒆𝒂_𝒌𝒎𝟐′: [𝟐𝟔𝟕𝟐. 𝟐𝟖, 𝟏𝟓𝟒𝟓. 𝟕𝟕, 𝟏𝟒𝟖𝟕. 𝟕, 𝟏𝟏𝟔. 𝟓, 𝟐𝟕𝟗. 𝟖𝟗, 𝟔𝟐𝟏𝟕. 𝟐𝟔, 𝟑𝟔𝟖. 𝟗, 𝟏𝟎𝟗. 𝟏𝟗, 𝟓𝟗. 𝟒, 𝟒𝟖𝟑. 𝟒𝟒],
′𝑨𝒍𝒕𝒊𝒕𝒖𝒅_𝒎′: [𝟏𝟓𝟒, 𝟐𝟑𝟐𝟓, 𝟑𝟒, 𝟑𝟑𝟗𝟗, 𝟐𝟗, 𝟐𝟗, 𝟏𝟎𝟔, 𝟑𝟐𝟕𝟏, 𝟓𝟔𝟐, 𝟏𝟓𝟔],
′𝑫𝒆𝒏𝒔𝒊𝒅𝒂𝒅_𝒑𝒐𝒃𝒍𝒂𝒄𝒊𝒐𝒏_𝒑𝒐𝒓_𝒌𝒎𝟐′: [𝟑𝟗𝟐𝟒, 𝟔𝟒. 𝟖, 𝟔𝟐. 𝟏, 𝟑𝟔𝟕𝟑, 𝟏𝟎𝟗𝟏. 𝟔, 𝟕𝟕. 𝟗, 𝟏𝟏𝟗𝟔, 𝟑𝟓𝟐𝟖. 𝟔, 𝟒𝟗𝟔𝟔, 𝟓𝟖𝟕. 𝟐]
"""

!pip install pandas

import pandas as pd

data_ciudades = {'Ciudad': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Iquitos', 'Huancayo', 'Tacna', 'Pucallpa'],
                 'Habitantes': [1047996, 100169, 92331, 428450, 305717, 484475, 441649, 385098, 294395, 283734],
                 'Area_km2': [2672.28, 1545.77, 1487.7, 116.5, 279.89, 6217.26, 368.9, 109.19, 59.4, 483.44],
                 'Altitud_m': [154, 2325, 34, 3399, 29, 29, 106, 3271, 562, 156],
                 'Densidad_poblacion_por_km2': [3924, 64.8, 62.1, 3673, 1091.6, 77.9, 1196, 3528.6, 4966, 587.2]
                 }

"""

*   Creamos dataframe

"""

nfo = pd.DataFrame(data_ciudades)

nfo

"""2. Realiza el mismo procedimiento con el siguiente diccionario. A partir de él, crea un dataframe llamado 𝒏𝒐𝒎𝒃𝒓𝒆𝒔.

data_ciudades_2 =  {
′𝑪𝒊𝒖𝒅𝒂𝒅′: [′𝑳𝒊𝒎𝒂′, ′𝑨𝒓𝒆𝒒𝒖𝒊𝒑𝒂′, ′𝑻𝒓𝒖𝒋𝒊𝒍𝒍𝒐′, ′𝑪𝒖𝒔𝒄𝒐′, ′𝑪𝒉𝒊𝒄𝒍𝒂𝒚𝒐′, ′𝑷𝒊𝒖𝒓𝒂′, ′𝑰𝒒𝒖𝒊𝒕𝒐𝒔′, ′𝑯𝒖𝒂𝒏𝒄𝒂𝒚𝒐′, ′𝑻𝒂𝒄𝒏𝒂′, ′𝑷𝒖𝒄𝒂𝒍𝒍
′𝑮𝒆𝒏𝒕𝒊𝒍𝒊𝒄𝒊𝒐′: [′𝑳𝒊𝒎𝒆𝒏𝒔𝒆′, ′𝑨𝒓𝒆𝒒𝒖𝒊𝒑𝒆ñ𝒐′, ′𝑻𝒓𝒖𝒋𝒊𝒍𝒍𝒂𝒏𝒐′, ′𝑪𝒖𝒔𝒒𝒖𝒆ñ𝒐′, ′𝑪𝒉𝒊𝒄𝒍𝒂𝒚𝒂𝒏𝒐′, ′𝑷𝒊𝒖𝒓𝒂𝒏𝒐′, ′𝑰𝒒𝒖𝒊𝒕𝒆ñ𝒐′, ′𝑯𝒖𝒂𝒏
′𝑷𝒓𝒐𝒗𝒊𝒏𝒄𝒊𝒂′: [′𝑳𝒊𝒎𝒂′, ′𝑨𝒓𝒆𝒒𝒖𝒊𝒑𝒂′, ′𝑻𝒓𝒖𝒋𝒊𝒍𝒍𝒐′, ′𝑪𝒖𝒔𝒄𝒐′, ′𝑪𝒉𝒊𝒄𝒍𝒂𝒚𝒐′, ′𝑷𝒊𝒖𝒓𝒂′, ′𝑴𝒂𝒚𝒏𝒂𝒔′, ′𝑯𝒖𝒂𝒏𝒄𝒂𝒚𝒐′, ′𝑻𝒂𝒄𝒏𝒂′, ′𝑪𝒐𝒓
′𝑹𝒆𝒈𝒊𝒐𝒏′: [′𝑳𝒊𝒎𝒂′, ′𝑨𝒓𝒆𝒒𝒖𝒊𝒑𝒂′, ′𝑳𝒂 𝑳𝒊𝒃𝒆𝒓𝒕𝒂𝒅′, ′𝑪𝒖𝒔𝒄𝒐′, ′𝑳𝒂𝒎𝒃𝒂𝒚𝒆𝒒𝒖𝒆′, ′𝑷𝒊𝒖𝒓𝒂′, ′𝑳𝒐𝒓𝒆𝒕𝒐′, ′𝑱𝒖𝒏í𝒏′, ′𝑻𝒂𝒄𝒏𝒂′, ′𝑼𝒄𝒂𝒚
"""

data_ciudades_2 = {'Ciudad': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Iquitos', 'Huancayo', 'Tacna', 'Pucallpa'],
                   'Gentilicio': ['Limense', 'Arequipeño', 'Trujillano', 'Cusqueño', 'Chiclayano', 'Piurano', 'Iquiteño', 'Huancaíno', 'Tacneño', 'Pucallpino'],
                   'Provincia': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Maynas', 'Huancayo', 'Tacna', 'Coronel Portillo'],
                   'Region': ['Lima', 'Arequipa', 'La Libertad', 'Cusco', 'Lambayeque', 'Piura', 'Loreto', 'Junín', 'Tacna', 'Ucayali']}

nombres = pd.DataFrame(data_ciudades_2)

nombres

"""3. Con ambos dataframes, realiza un inner join. Guarda el resultado en un nuevo dataframe
llamado 𝒄𝒖𝒂𝒅𝒓𝒐_𝟏.
"""

cuadro_1 = pd.merge(nfo, nombres, on='Ciudad', how='inner')

cuadro_1

"""4) Resume las estadísticas descriptivas del dataframe y responde ¿Cuál es la mínima
densidad poblacional? ¿A cuál ciudad corresponde? ¿Y la máxima?
"""

stats = cuadro_1.describe()

# Encontrar la densidad poblacional mínima y máxima
densidad_min = cuadro_1.loc[cuadro_1['Densidad_poblacion_por_km2'].idxmin()]
densidad_max = cuadro_1.loc[cuadro_1['Densidad_poblacion_por_km2'].idxmax()]

print("Estadísticas descriptivas:")
print(stats)
print("\nLa densidad poblacional mínima es de {} y corresponde a la ciudad de {}.".format(densidad_min['Densidad_poblacion_por_km2'], densidad_min['Ciudad']))
print("La densidad poblacional máxima es de {} y corresponde a la ciudad de {}.".format(densidad_max['Densidad_poblacion_por_km2'], densidad_max['Ciudad']))

"""5) Realizar un gráfico de barras donde se vea la cantidad de habitantes en cada ciudad"""

import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(cuadro_1['Ciudad'], cuadro_1['Habitantes'], color='skyblue')


plt.title('Cantidad de Habitantes por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Cantidad de Habitantes')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

"""6. Realizar un gráfico de dispersión entre la altura y el número de habitantes en las ciudades del dataframe."""

import pandas as pd
import matplotlib.pyplot as plt

# Crear los diccionarios
data_ciudades = {
    'Ciudad': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Iquitos', 'Huancayo', 'Tacna', 'Pucallpa'],
    'Habitantes': [1047996, 100169, 92331, 428450, 305717, 484475, 441649, 385098, 294395, 283734],
    'Area_km2': [2672.28, 1545.77, 1487.7, 116.5, 279.89, 6217.26, 368.9, 109.19, 59.4, 483.44],
    'Altitud_m': [154, 2325, 34, 3399, 29, 29, 106, 3271, 562, 156],
    'Densidad_poblacion_por_km2': [3924, 64.8, 62.1, 3673, 1091.6, 77.9, 1196, 3528.6, 4966, 587.2]
}

data_ciudades_2 = {
    'Ciudad': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Iquitos', 'Huancayo', 'Tacna', 'Pucallpa'],
    'Gentilicio': ['Limense', 'Arequipeño', 'Trujillano', 'Cusqueño', 'Chiclayano', 'Piurano', 'Iquiteño', 'Huancaíno', 'Tacneño', 'Pucallpino'],
    'Provincia': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Maynas', 'Huancayo', 'Tacna', 'Coronel Portillo'],
    'Region': ['Lima', 'Arequipa', 'La Libertad', 'Cusco', 'Lambayeque', 'Piura', 'Loreto', 'Junín', 'Tacna', 'Ucayali']
}

# Crear los DataFrames
nfo = pd.DataFrame(data_ciudades)
nombres = pd.DataFrame(data_ciudades_2)

# Realizar el Inner Join
cuadro_1 = pd.merge(nfo, nombres, on='Ciudad')

# Realizar el gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(cuadro_1['Altitud_m'], cuadro_1['Habitantes'], color='blue')
plt.title('Gráfico de Dispersión entre Altura y Habitantes por Ciudad')
plt.xlabel('Altitud (m)')
plt.ylabel('Número de Habitantes')
plt.grid(True)
plt.show()