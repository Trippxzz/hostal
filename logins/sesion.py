from principal.main import bconsola
from principal.connector import Operaciones
from logins.menus import menuPrincipalIn
from logins.registrar import registrar_usuario
import time
con = Operaciones
listausuarios = []


# INICIO DE SESION USUARIO

def iniciar_sesion():
    intentos = 0
    listausuarios = con.getInfoUsuario()

    while intentos < 3:
        mail = input("Ingrese su correo: ")
        encontrado = False  # Bandera para indicar si se encontró una coincidencia

        for user in listausuarios:
            if mail == user.correo:
                contra = input("Ingrese la contraseña: ")
                if contra == user.contra:
                    print("Inicio de sesión completado.")
                    time.sleep(2)
                    bconsola()
                    menuPrincipalIn()
                    return 
                else:
                    print("Contraseña incorrecta.")
                    break  # Salir del bucle for cuando la contraseña sea incorrecta
            else:
                intentos += 1
                print(intentos)
                encontrado = True
                break

        if not encontrado:
            print("Este correo no es válido")
        
    print("Has alcanzado el límite de intentos.")
    reg = input("Escribe 'Registrar' para ir al panel de Registro")
    if reg == "Registrar":
        registrar_usuario()
    # nomas = input("Si deseas registrarte, escribe 'Registrarme': ")
    # if nomas == "Registrarme":
        # bconsola()
        # registrar.registrar_usuario()

