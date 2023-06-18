from principal.main import bconsola
from principal.connector import Operaciones
from logins.menus import menuPrincipalIn
from logins.registrar import registrar_usuario
import time
con = Operaciones
listausuarios = []


# INICIO DE SESION

def iniciar_sesion():
    intentos = 0
    listausuarios = con.getInfoUsuario()
    bconsola()
    print("=============== Inicia Sesión ================")
    while intentos < 3:
        mail = input("Ingrese su correo: ")

        for user in listausuarios:
            if mail == user.correo:
                contra = input("Ingrese la contraseña: ")
                if contra == user.contra:
                    print("Inicio de sesión completado.")
                    time.sleep(3)
                    bconsola()
                    menuPrincipalIn()
                    return 
                else:
                    print("Contraseña incorrecta.")
                    break 
            else:
                intentos += 1
                print("Este correo no es válido")
                break

            

    print("\n===============Has alcanzado el límite de intentos.===============")
    termino_intentos()


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