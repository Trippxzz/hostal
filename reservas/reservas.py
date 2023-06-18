# Registrar reserva dentro del hostal

def registrar_reserva(nombre, fecha, metodoPago):

    print("Reserva registrada exitosamente")

    
# Mostrar las reservas concretadas

def mostrar_reservas(self):

    if not reservas:
        print("No hay reservas registradas")
    else:
        for reserva in reservas:
            print("Nombre:", reserva[0])
            print("Fecha:", reserva[1])
            print("Metodo de Pago:", reserva[2])
            print()  

    conn.close()


# inicar sesion como trabajador

def iniciar_sesion_recepcionista(usuario, contraseña):


    if resultado:
        print("Inicio de sesión exitoso como trabajador")
        
    else:
        print("Credenciales incorrectas, inicio de sesión fallido")

    conn.close()
