from principal.main import bconsola
from principal.connector import Operaciones
import time

con = Operaciones
listarecepcionistas = []


            
    # Login de los recepcionistas 
    
def login_recepcionista():
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
                    # funcion menu trabajador
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
    
