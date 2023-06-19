from principal.main import bconsola
from principal.connector import Operaciones
from reservas.hacerreserva import menuHostales
from logins.registrar import registrar_usuario
import time

con = Operaciones
listausuarios = []


correosesion = None
# INICIO DE SESION

def iniciar_sesion(cis, n):
    intentos = 0
    listausuarios = con.getInfoUsuario()
    bconsola()
    print("=============== Inicia Sesión ================")
    while intentos < 3:
        mail = input("Ingrese su correo: ")
        cval = False
        for user in listausuarios:
            if mail == user.correo:
                cval = True
                contra = input("Ingrese la contraseña: ")
                if contra == user.contra:
                    cis = "Usuario"
                    n = mail
                    print("Inicio de sesión completado.")
                    time.sleep(3)
                    bconsola()
                    menuPrincipalIn(cis, n)
                    return 
                else:
                    print("Contraseña incorrecta.")
                    break 
  
        intentos += 1
        if not cval:
            print("Este correo no es válido")
                

            

    print("\n===============Has alcanzado el límite de intentos.===============")
    termino_intentos()


def menuPrincipalIn(cis, n):
    print("==================== MENÚ PRINCIPAL HOSTALES  ====================")
    print("========================= SESION INICIADA ========================")
    print("1.- Ver hostales")
    print("1.- Ver tus Datos")
    print("2.- Salir")
    print("========================================================")
    seleccionar = int(input("Seleccione una opción: "))
    if seleccionar == 1:
        menuHostales(cis, n)


def termino_intentos():
    print("1.- Para ir al panel de Registro")
    print("2.- Para volver a intentar")
    reg = int(input("Seleccione una opción: "))
    if reg == 1:
        print("Te estamos redirigiendo al panel de registro")
        time.sleep(3)
        bconsola()
        registrar_usuario()
    elif reg == 2:
        iniciar_sesion()

