import string, secrets, time
from datetime import datetime
from principal.connector import Operaciones
from principal.main import bconsola
# from principal.menui import MenuPrincipal

op = Operaciones
listahostales = []
listahabitaciones = []
listacomprobacion = []
listaco2= []
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
        hs = hostales[seleccionar- 1]
        listahabitaciones = op.getHabitaciones(hs.idhostal)
        bconsola()
        print("==================== Información de ",hs.nombre," ====================")
        print("Dirección: ", hs.direccion )
        for hab in listahabitaciones:
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
            idh = hs.idhostal

            reservar =  int(input("Seleccione una opción: ")) 
            if reservar == 1:
                pdatosr(cis, n, canthab, hdispo, hn, nh, idh)
            elif reservar == 2:
                menuHostales(cis, n)
            elif reservar == 3:
                menuHostales(cis, n)
    elif seleccionar == 6:
        MenuPrincipal()


def pdatosr(cis, n, canthab, hdispo, hn, nh, idh):
    if cis != None: 
        # print(canthab, hdispo, hn, nh, idh)
        if hdispo == "Disponible":
            bconsola()
            cant = int(input("Ingrese la cantidad de huespedes que serán: "))
            if cant <= canthab:
                fechallegada = input("Ingrese la fecha de llegada (YYYY-MM-DD): ")
                fechasalida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
                fllpartes = fechallegada.split("-")
                fspartes = fechasalida.split("-")
                anoll = fllpartes[0] #AÑO LLEGADA
                anos = fspartes[0] # AÑO SALIDA
                mesll = fllpartes[1] # MES LLEGADA
                mess = fspartes[1] # MES SALIDA
                diall = fllpartes[2] # DIA LLEGADA
                dias = fspartes[2] # DIA SALIDA
                dll = datetime.strptime(fechallegada, "%Y-%m-%d")
                ds = datetime.strptime(fechasalida, "%Y-%m-%d")
                diferencia = dll - ds
                cantdias = diferencia.days
                if anoll >= "2023" and mesll >= "01" and mesll <= "12":
                    if anos >= "2023" and mess >= "01" and mess <= "12":
                        if mesll == mess and anoll == anos:
                            if dll < ds:
                                pdatosp(cis, n, canthab, hdispo, hn, nh, idh, cantdias, fechallegada, fechasalida )
                            else:
                                print("El día de llegada debe ser antes del día de salida")
                                time.sleep(4)
                                pdatosr(cis, n, canthab, hdispo, hn, nh, idh)
                                return
                        elif anoll == anos and mesll <= mess:
                            print("El mes de llegada debe ser anterior o igual al mes de salida")
                            time.sleep(4)
                            pdatosr(cis, n, canthab, hdispo, hn, nh, idh)
                            return
                        elif mesll != mess and anoll < anos:
                                pdatosp(cis, n, canthab, hdispo, hn, nh, idh, cantdias, fechallegada, fechasalida )
                        else:
                            print("Ha ocurrido un error en el ingreso de fechas")
                            time.sleep(4)
                            pdatosr(cis, n, canthab, hdispo, hn, nh, idh)
                            return
                    else:
                        print("El año de salida seleccionado o mes de salida seleccionado no es válido")
                        time.sleep(4)
                        pdatosr(cis, n, canthab, hdispo, hn, nh, idh)
                        return
                else:
                    print("El año de llegada seleccionado o mes de llegada seleccionado no es válido")
                    time.sleep(4)
                    pdatosr(cis, n, canthab, hdispo, hn, nh, idh)
                    return
            else:
                print("La cantidad de huespedes excede la cantidad disponible")
                time.sleep(4)
                pdatosr(cis, n, canthab, hdispo, hn, nh, idh)
                return

        else:
            print("Esta habitacion no esta disponible")
            time.sleep(4)
            pdatosr(cis, n, canthab, hdispo, hn, nh, idh)
            return
    else:
        print("Para poder reservar debes tener una cuenta creada")
        time.sleep(3)
        menuHostales(cis, n)

    
def pdatosp(cis, n, canthab, hdispo, hn, nh, idh, cantdias, fechallegada, fechasalida ):
    monto:int = cantdias * -50000  
    if cis != "Recepcionista":
        listacomprobacion = op.getRut(n)
        for user in listacomprobacion:
            pdigitos = user.rut[:5]
            if pdigitos == "SUSER":    
                rut = input("Ingrese su rut: ")
                nombre = input("Ingrese su Nombre y Apellido: ")
                ntelefno = input("Ingrese su numero de contacto")
                fnac = input("Ingrese su fecha de nacimiento: ")
                dire = input("Ingrese su dirección de hogar: ")
                p = input("Ingrese el país donde vive: ")                           
                print("¡Datos personas ingresados Correctamente!")
                time.sleep(2)
                bconsola()
                print("================Metodo de pago===================")
                print("1.- Debito")
                print("2.- Credito")
                print("3.- Salir")
                print("-Monto a pagar: $",monto)
                print("==================================================")
                seleccionar = int(input("Seleccione una opcion: "))
                if seleccionar == 1:
                    mpago = "Debito"
                elif seleccionar == 2:
                    mpago = "Credito"
                elif seleccionar == 3:
                    menuHostales(cis, n)                    
                if seleccionar == 1 or seleccionar == 2:
                    time.sleep(3)
                    bconsola()
                    print("================Confirmación===================")    
                    print("1.- Confirmar Pago y Realizar Reserva")
                    print("2.- Salir")
                    print("==================================================")
                    s = int(input("Seleccione una opcion: "))
                    if s == 1:
                        ide = generar_id()
                        print("================ Reserva realizada ===============")
                        print("ID de Reserva: ", ide)
                        print("Hostal: ", hn)
                        print("Habitación: ", nh)
                        print("Nombre de quien reserva: ", nombre)
                        print("Fecha de llegada: ", fechallegada)
                        print("Fecha de salida: ", fechasalida)
                        print("Monto Total: ", monto)
                        print("==================================================") 
                        op.actualizar_a_cliente(rut, nombre, user.correo, user.contra, fnac, dire, p, ntelefno)
                        op.crear_reservas(ide, idh, nh, rut, "web", fechallegada, fechasalida)     
                        op.genregPago(ide,monto,mpago ,factual)  
                        ActDispo(idh, canthab)
                        print("En 30 segundos serás redirigido/a al menú principal")
                        time.sleep(30)
                        bconsola()
                    elif s == 2:
                        menuHostales(cis, n)                                             
            else:
                print("================Metodo de pago===================")
                print("1.- Debito")
                print("2.- Credito")
                print("3.- Salir")
                print("-Monto a pagar: $",monto)
                print("==================================================")
                seleccionar = int(input("Seleccione una opcion: "))
                if seleccionar == 1:
                    mpago = "Debito"
                elif seleccionar == 2:
                    mpago = "Credito"
                elif seleccionar == 3:
                    menuHostales(cis, n)                    
                if seleccionar == 1 or seleccionar == 2:
                    time.sleep(3)
                    bconsola()
                    print("================Confirmación===================")    
                    print("1.- Confirmar Pago y Realizar Reserva")
                    print("2.- Salir")
                    print("==================================================")
                    s = int(input("Seleccione una opcion: "))
                    if s == 1:
                        ide = generar_id()
                        print("================ Reserva realizada ===============")
                        print("ID de Reserva: ", ide)
                        print("Hostal: ", hn)
                        print("Habitación: ", nh)
                        print("Nombre de quien reserva: ", user.nombrec)
                        print("Fecha de llegada: ", fechallegada)
                        print("Fecha de salida: ", fechasalida)
                        print("Monto Total: ", monto)
                        print("==================================================") 
                        op.crear_reservas(ide, idh, nh, user.rut, "web", fechallegada, fechasalida)  
                        factual = datetime.now().date()  
                        op.genregPago(ide,monto,mpago ,factual)  
                        ActDispo(idh, canthab)
                        print("En 30 segundos serás redirigido/a al menú principal")
                        time.sleep(30)
                        bconsola()
                    # elif s == 2:
                    #     menuHostales(cis, n)     
    else:
        ide = generar_id()
        rut = input("Ingrese el rut del cliente: ")
        print("================Metodo de pago===================")
        print("1.- Debito")
        print("2.- Credito")
        print("3.- Efectivo")
        print("4.- Transferencia")
        print("5.- Salir")
        print("-Monto a pagar: $",monto)
        print("==================================================")
        s = int(input("Seleccione una opcion: ")) 
        if s == 1:
            mpago = "Debito"
        elif s ==2:
            mpago = "Credito"
        elif s == 3:
            mpago == "Efectivo"
        elif s == 4:
            mpago = "Transferencia"
        elif s == 5:
            menuHostales(cis, n)  
        if s != 5:
            listacomprobacion = op.getInfoTrabajadorC(n)
            for recep in listacomprobacion:
                op.crear_reservas(ide, idh, nh, rut, recep.rut, fechallegada, fechasalida)
                factual = datetime.now().date()
                op.genregPago(ide,monto,mpago ,factual)                
                ActDispo(idh, canthab)


def ActDispo(idh, canthab):
    listaco2 = op.getHabitaciones(idh)  
    for h in listaco2:
        cantfinal = h.maxhab - canthab
        if cantfinal >= 1:
            dispo = "Disponible"
        else:
            dispo = "Ocupada"
        op.actualizar_disponibilidad(cantfinal, dispo, idh)


def generar_id():
    caracteres = string.ascii_lowercase + string.digits
    id_random = ''.join(secrets.choice(caracteres) for _ in range(4))
    return  id_random 