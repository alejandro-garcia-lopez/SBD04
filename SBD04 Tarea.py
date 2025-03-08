import pandas as pd

indice = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
columnas = ['Raza', 'Puntos']
lista = [['Caniche', 8.1], ['Bulldog', 7.3], ['ChowChow', 7.6], ['Chihuahua', 9.0], ['Labrador', 9.3]]

print('----------------------------')
print('---      Apartado 1       --')
print('----------------------------')
# Apartado 1: Crear un DataFrame

df = pd.DataFrame(lista, index=indice, columns=columnas)
print(df)

print('----------------------------')
print('---      Apartado 2       --')
print('----------------------------')
# Apartado 2: Agregar columnas al DataFrame

puntos_ana = [61, 75, 82, 95, 99]
df['PuntosAna'] = puntos_ana
print(df)

print('----------------------------')
print('---      Apartado 3       --')
print('----------------------------')
# Apartado 3: Normalizar datos

puntos_ana_normalizados = df['PuntosAna'] / 10
df['PuntosAna'] = puntos_ana_normalizados
print(df)

print('----------------------------')
print('---      Apartado 4       --')
print('----------------------------')
# Apartado 4: Añadir entradas al dataframe

lista2 = [['Samoyedo', 9.2, 8.9], ['Pinscher', 8.1, 6.7]]
nuevos_indices = ['nuevo1', 'nuevo2']
columnas_df = ['Raza', 'Puntos', 'PuntosAna']

#columnas_df = []
#for c in df:
#  column_list.append(c)
#print(column_list)

df_nuevas_entradas = pd.DataFrame(lista2, index=nuevos_indices, columns=columnas_df)
df = pd.concat([df, df_nuevas_entradas]) # Concatenar dataframes
print(df)

print('----------------------------')
print('---      Apartado 5       --')
print('----------------------------')
# Apartado 5: Calcular media

df['Media'] = df[['Puntos', 'PuntosAna']].mean(axis=1)
print(df)

print('----------------------------')
print('---      Apartado 6       --')
print('----------------------------')
# Apartado 6: Eliminar entrada

df = df.drop('dos')
print(df)

print('----------------------------')
print('---      Apartado 7       --')
print('----------------------------')
# Apartado 7: Tomar filas del dataframe

#df_final = df.loc[['cuatro', 'cinco', 'nuevo1']]
df_final = df[2:5]
print(df_final)

print('----------------------------')
print('---      Apartado 8       --')
print('----------------------------')
# Apartado 8: Descripciónd el dataframe

print(df_final.describe())


