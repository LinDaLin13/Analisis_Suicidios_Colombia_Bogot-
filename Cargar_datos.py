import pandas as pd

#cargar archivo de excel
df = pd.read_csv(r"C:\Users\Linda\Desktop\Suicidio_Colombia\conducta_suicida.csv")

#mostrar las primeras filas
print(df.head())

#mostrar informacion general del archivo
print(df.info())

#verificar los valores que son nulos
print(df.isnull().sum())

#ver valores nulos por columna
print(df.isnull().sum())

#ver tipos de datos
print(df.dtypes)

#Descripcion estadistica de los datos 
print(df.describe())
