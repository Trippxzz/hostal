import string, secrets, time
from principal.connector import Operaciones
from principal.main import bconsola, Usuario

op = Operaciones
listahostales = []
listahabitaciones = []
listacomprobacion = []
hdispo, canthab, nh, hn, idh = None, 0, None, 0, None

def menuHostales(cis, n):
    bconsola()
    listahostales = op.getHostales()
    print("==================== HOSTALES ====================")
    hostales = []
    for h in listahostales:
        hostales.append(h)
        print(len(hostales),".- ", h.nombre)
    print("6.- Regresar al Menu Principal")
    print("==================================================")
    seleccionar = int(input("Seleccione un hostal: "))  

    if seleccionar >= 1 and seleccionar <= len(hostales):
        hs = hostales[seleccionar - 1]
        listahabitaciones = op.getHabitaciones(hs.idhostal)
        bconsola()
        print("==================== Información de ",hs.nombre," ====================")
        print("Dirección: ", hs.direccion )
        for hab in listahabitaciones:
            print("==================================================")
            print("Habitaciones Disponibles: ", hab.maxhab)
            print("Disponibilidad: ", hab.disponibilidad)
            print("\n==================== ¿Desea continuar con la reserva? ====================")
            print("1.- Continuar con la reserva")
            print("2.- Ver otro Hostal")
            print("3.- Salir")
            print("==================================================")

            canthab:int = hab.maxhab
            hdispo = hab.disponibilidad
            hn = h.nombre
            nh = hab.idhabitacion
            idh = h.idhostal

            reservar =  int(input("Seleccione una opción: ")) 
            if reservar == 1:
                realizar_reserva(cis, n, canthab, hdispo, hn, nh, idh)
            elif reservar == 2:
                menuHostales(cis, n)
            # elif reservar == 3:
                # en desarrollo


def realizar_reserva(cis, n, canthab, hdispo, hn, nh, idh):
    if cis != None: 
        # print(canthab, hdispo, hn, nh, idh)
        if hdispo == "Disponible":
            bconsola()
            cant = int(input("Ingrese la cantidad de huespedes que serán: "))
            if cant <= canthab:
                fechallegada = input("Ingrese la fecha de llegada (YYYY-MM-DD): ")
                fechasalida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
                
                if cis != "Recepcionista":
                    listacomprobacion = op.getRut(n)
                    for user in listacomprobacion:
                        pdigitos = user.rut[:5]
                        if pdigitos == "SUSER":    
                            rut = input("Ingrese su rut: ")
                            nombre = input("Ingrese su nombre y apellido: ")
                            fnac = input("Ingrese su fecha de nacimiento: ")
                            dire = input("Ingrese su dirección de hogar: ")
                            p = input("Ingrese el país donde vive: ")

                            op.actualizar_a_cliente(rut, nombre, user.correo, user.contra, fnac, dire, p)
                            op.crear_reservas(generar_id(), idh, nh, rut, "web", nombre, fechallegada, fechasalida)

                            print("Tus datos han sido ingresado correctamente!")

                            # print("================ Reserva realizada ===============")
                            # print("Identificador: ", generar_id())
                            # print("Hostal: ", hn)
                            # print("Habitación: ", nh)
                            # print("Nombre: ", nombre)
                            # print("Fecha de llegada: ", fechallegada)
                            # print("Fecha de salida: ", fechasalida)
                            # print("==================================================")
                            break
                    else:
                        op.crear_reservas(generar_id(), idh, nh, rut, "web", nombre, fechallegada, fechasalida)
                else:
                    # HACER FOR PARA BUSCAR RUT DE EMPLEADO CON EL CORREO ASIGNADO EN VARIABLE "n"
                    op.crear_reservas(generar_id(), idh, nh, rut, "web", nombre, fechallegada, fechasalida)
            else:
                print("La cantidad de huespedes excede la cantidad disponible")
                return

        else:
            print("Esta habitacion no esta disponible")
            return

        

################################################################
        
    else:
        print("Para poder reservar debes tener una cuenta creada")
        time.sleep(3)
        menuHostales(cis, n)

    
    
def generar_id():
    caracteres = string.ascii_lowercase + string.digits
    id_random = ''.join(secrets.choice(caracteres) for _ in range(4))
    return  id_random 