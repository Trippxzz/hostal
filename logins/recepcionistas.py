from principal.main import bconsola
from principal.connector import Operaciones
import time
from reservas.verreservas import verReservas
from reservas.hacerreserva import menuHostales
con = Operaciones
listarecepcionistas = []


            
    # Login de los recepcionistas 
    
def login_recepcionista(cis, n):
    intentos = 0
    listarecepcionistas = con.getInfoTrabajador()
    bconsola()
    print("=============== Inicie Sesión como Colaborador ================")
    while intentos < 3:
        correo = input("Ingrese su correo: ")
        cval = False
        for r in listarecepcionistas:
            if correo == r.mail:
                cval = True
                contra = input("Ingrese su contraseña: ")
                if contra == r.contrasena:
                    print("Bienvenido/a", r.nombre, r.apellido)
                    print("Te redirigiremos al panel de Trabajador")
                    time.sleep(3)
                    bconsola()
                    cis = "Recepcionista"
                    n = correo
                    menuRecepcionistas(cis, n)
                    return
                else:
                     print("Contraseña incorrecta")
                     break
        intentos += 1
        if not cval:
            print("Este correo no es válido")

    print("\n===============Has alcanzado el límite de intentos.===============")
    time.sleep(2)
    login_recepcionista()            
    
def menuRecepcionistas(cis, n):
    print("========================= RECEPCIONISTAS ========================")
    print("1.- Realizar reservas")
    print("2.- Ver Reservas")
    print("3.- Regresar al Menu Principal")
    print("==================================================")
    seleccionar = int(input("Seleccione una opción: "))

    if seleccionar == 1:
        menuHostales(cis, n)
    elif seleccionar == 2:
        verReservas()
    # elif seleccionar == 3:
    #     MenuPrincipal()

