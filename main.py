from hotel import reservas, habitaciones, clientes

def menu():
    df = reservas.cargar_reservas()
    while True:
        print("\n1. Añadir Reserva")
        print("2. Cancelar Reserva")
        print("3. Mostrar todas las Reservas")
        print("4. Salir")
        
        opcion= input("Eliga su opcion: ")
        
        if opcion == "1":
            nombre = input("Nombre del Cliente: ")
            tipo = input("Tipo de habitacion: ")
            entrada = input("fecha de entrada (DD-MM-YYYY): ")
            salida = input("fecha de salidad (DD-MM-YYYY): ")
            
            if habitaciones.verificar_disponibilidad(tipo,entrada,salida):
                df = reservas.anadir_reserva(df,nombre,tipo,entrada,salida)
                reservas.guardar_reserva(df)
                print("su reserva fue agregada exitosamente")
                
            else:
                print("No hay disponibilidad para el tipo y feha eleegida")
                
        elif opcion=="2":
            reserva_id = int(input("ID de la reserva a cancelar:  "))
            df = reservas.cancelar_reserva(df, reserva_id)
            reservas.guardar_reserva(df)
            print("Reserva Cancelada")
            
        elif opcion =="3":
            reservas.mostrar_reservas(df)
            
        elif opcion == "4":
            print("Saliendo del sistema =)")
            break
        else:
            print("opcion invalidad")

        
if __name__ == "__main__":
    menu()
            
        
            
