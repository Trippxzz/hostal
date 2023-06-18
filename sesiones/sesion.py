from principal.main import bconsola
from principal.connector import Operaciones
import registrar, mprin, time
hostales = []
con = Operaciones()
listausuarios = []


# INICIO DE SESION

def iniciar_sesion():
    intentos = 0
    listausuarios = con.getInfoUsuario()

    mail = input("Ingrese su correo: ")

    for user in listausuarios:
        while intentos < 3:
            if mail == user.correo:
                contra = input("Ingrese la contraseña: ")
                if contra == user.contra:
                    print("Inicio de sesión completado.")
                    time.sleep(2)
                    bconsola()
                    mprin.menuPrincipalIn()
                    return 
                else:
                    print("Contraseña incorrecta.")
                    return
            else:
                print("Correo no válido")
                intentos += 1
        else:
            print("Has alcanzado el límite de intentos.")
            nomas = input("Si deseas registrarte, escribe 'Registrarme': ")
            if nomas.lower() == "registrarme":
                bconsola()
                registrar.registrar_usuario()
            return 
    else:
        print("Este correo no es válido")



