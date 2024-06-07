#maneja operaciones relacionadas con clientes como actualizar existente o agregar uno nuevo 

import pandas as pd 

def cargar_clientes(filename="clientes.csv"):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=["ID","Nombre","Contacto"])
    
def guardar_clientes(df,filename="clientes.csv"):
    df.to_csv(filename,index=False)
    
def agregar_cliente(nombre,contacto):
    df = cargar_clientes()
    cliente_id = len(df)+1
    nuevo_cliente=pd.DataFrame({
        "ID":[cliente_id],
        "Nombre":[nombre],
        "Contacto":[contacto]
    })
    df = df.apppend(nuevo_cliente, ignore_index=True)
    guardar_clientes(df)
    return cliente_id
    
def actualizar_cliente(cliente_id,nuevos_datos):
    df=cargar_clientes()
    df.loc[df["ID"] == cliente_id,["Nombre","Contacto"]]=[nuevos_datos["Nombre"],nuevos_datos["Contacto"]]
    guardar_clientes(df)
    