#modulo que gestiona las reservas 

import pandas as pd 


def encargar_reservas(filename="reservas.csv"):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=["ID","Nombre","Tipo","Entrada","Salida","Estado"])
    
    
def guardar_reserva(df, filename="reservas.csv"):
    df.to_csv(filename, index=False)
    
    
def anadir_reserva(df,nombre,tipo,entrada,salida):
    reserva_id=len(df)+1
    nueva_reserva=pd.DataFrame({
        "ID":[reserva_id],
        "Nombre":[nombre],
        "Tipo":[tipo],
        "Entrada":[entrada],
        "Salida":[salida],
        "Estado":["Activo"]
    })
    return df.append(nueva_reserva, ignore_index=True)
    
    
def cancelar_reserva(df,reserva_id):
    df.loc[df["ID"]== reserva_id,"Estado"]="Cancelada"
    return df 
    
    
def mostrar_reservas(df):
    print(df)