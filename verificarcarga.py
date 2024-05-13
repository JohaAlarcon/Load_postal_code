import pandas as pd

def cargar_datos(ruta_archivo):
    # Asegúrate de que estás pasando la variable ruta_archivo correctamente a pd.read_csv
    return pd.read_csv(ruta_archivo, encoding='macroman', delimiter=';')

# Define la ruta del archivo CSV aquí
ruta_archivo = '/Users/jona/Desktop/C_digos_Postales_Nacionales.csv'

# Utiliza la función cargar_datos para leer el archivo
df = cargar_datos(ruta_archivo)

# Imprime las primeras filas del DataFrame para verificar que se ha cargado correctamente
print(df.head())

