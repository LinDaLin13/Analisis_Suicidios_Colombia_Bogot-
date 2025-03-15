import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Cargar el dataset (ajusta la ruta si es necesario)
df = pd.read_csv("conducta_suicida.csv", delimiter=";")  # Asegúrate del delimitador correcto

# Resumen estadístico de los datos
print(df.describe(include="all"))

# Distribución de la edad
plt.figure(figsize=(8, 5))
df['edad'].hist(bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.title("Distribución de Edades")
plt.show()

# Distribución por género
plt.figure(figsize=(6, 4))
df['sexo'].value_counts().plot(kind='bar', color=['blue', 'pink'])
plt.xlabel("Género")
plt.ylabel("Cantidad")
plt.title("Distribución de Casos por Género")
plt.show()

