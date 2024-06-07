#gestiona disponibilidad y datos relacionados con las habitaciones 

#crear un archivo csv del mismo nombre para que tener la info sino no funca y guardarlo dentro de la carpeta de hotel donde esta este proyecto 

#crear el archivo con comas ID,Tipo,Disponible,Precio  1,Suite,Si,1000   2,Master,Si,1200   3,Premium,No,1400  

import pandas as pd 

def cargar_habitaciones(filename="habitaciones.csv"):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=["ID","Tipo","Disponibilidad","Entrada","Salida"])
    
def guardar_habitaciones(df, filename="habitaciones.csv"):
    df.to_csv(filename,index=False)
    
def verificar_disponibilidad(tipo,entrada,salida):
    df = cargar_habitaciones()
    print(df)
    disponibles = df[(df["Tipo"] == tipo) & (df["Disponibilidad"] == "Si")]
    return not disponibles.empty

#chequear la comparacion con la fecha con fechas existentes en el documento y looopear para que ninguna conincda nunca 
    
def actualizar_disponibilidad(habitacion_id,disponible):
    df = cargar_habitaciones()
    df.loc[df["ID"] == habitacion_id, "Disponible"] = "Si" if disponible else "No"
    guardar_habitaciones(df)