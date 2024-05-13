from sqlalchemy import create_engine
import pandas as pd

def conectar_db():
    # Cambia los siguientes detalles según tu configuración de MySQL
    usuario = 'Database user'
    contraseña = 'Password'
    host = 'hots or IP'
    nombre_db = 'Database name'
    url_conexion = f'mysql+mysqlconnector://{usuario}:{contraseña}@{host}/{nombre_db}'
    engine = create_engine(url_conexion)
    return engine

def cargar_datos(ruta_csv):
    dtype_spec = {'cod_departamento': str, 'cod_municipio': str, 'cod_postal': str}  # Mantener los códigos con ceros a la izquierda
    return pd.read_csv(ruta_csv, encoding='macroman', delimiter=';', dtype=dtype_spec)

def filtrar_datos(df, engine):
    query = "SELECT cod_departamento, cod_municipio FROM municipio"
    municipios_validos = pd.read_sql(query, con=engine, dtype={'cod_departamento': str, 'cod_municipio': str})
    df_valido = df.merge(municipios_validos, on=['cod_departamento', 'cod_municipio'], how='inner')
    return df_valido

def insertar_datos(df, tabla, engine):
    if not df.empty:
        df.to_sql(tabla, con=engine, index=False, if_exists='append')
        print("Los datos válidos han sido insertados con éxito.")
    else:
        print("No hay datos válidos para insertar debido a la falta de coincidencias.")

def main():
    ruta_csv = '/Users/jona/Desktop/C_digos_Postales_Nacionales.csv'
    nombre_tabla = 'codigo_postal'
    engine = conectar_db()
    df = cargar_datos(ruta_csv)
    df_filtrado = filtrar_datos(df, engine)
    insertar_datos(df_filtrado, nombre_tabla, engine)

if __name__ == "__main__":
    main()
