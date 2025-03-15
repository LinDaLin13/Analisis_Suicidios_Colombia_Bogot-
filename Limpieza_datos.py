import pandas as pd

#Organizar datos por columnas
df = pd.read_csv(r"C:\Users\Linda\Desktop\Suicidio_Colombia\conducta_suicida.csv", sep=";", encoding="utf-8")
#Mostrar las primeras filas
print(df.head())

#Ver nombres de columnas
print(df.columns)

#Eliminar columnas innecesarias (solo si asi lo requieres, este dataset es importante mantenerlo completo)
#df = df.drop(["usas_el_nombre_de_la_columna_a_eliminar"], axis=1)

#verificar los datos nulos
print(df.isnull().sum())

#Eliminar filas con datos nulos
df = df.dropna()

#Llenar valors nulos con un valor especifico
df = df.fillna(0)

#revisar y corregir los tipos de datos
print(df.dtypes)
#eliminar duplicidad de datos
df = df.drop_duplicates()
#guardar el archivo limpio
df.to_csv(r"C:\Users\Linda\Desktop\Suicidio_Colombia\conducta_suicida_limpio.csv", index=False)