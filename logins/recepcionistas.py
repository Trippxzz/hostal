# Registrar a los recepcionistas
from principal.main import bconsola
from principal.connector import Operaciones
import time

con = Operaciones
listarecepcionistas = []


def registrar_recepcionista():
    mail = input("Ingrese el correo que desea utilizar: ")
    contra = input("Ingrese la contraseña: ")
    contrac = input("Confirme la contraseña: ")
    
    listarecepcionistas = con.getInfoTrabajador()
    
    if mail != user.correo:
        if contra == contrac:
            print("Te has registrado correctamente, te moveremos al panel de Hostales")
            con.crearRecepcionista("SOLOUSER",mail, contra)

            time.sleep(2)
            bconsola()
            return
        else:
                print("Contraseñas incorrectas")
                registrar_recepcionista()
                return  # Salir del bucle for cuando la contraseña sea incorrecta
    else:
             print("Este correo ya ha sido utilizado, porfavor intente con otro")
             return 
         
    
    # Login de los recepcionistas 
    
def login_recepcionista():
    correo = input("Ingrese su correo: ")
    contra = input("Ingrese su contraseña: ")
    
    listarecepcionistas = con.getInfoRecepcionista()
    for recepcionista in listarecepcionistas:
        if correo == recepcionista.correo and contra == recepcionista.contraseña:
            print("Inicio de sesión exitoso como recepcionista")
            
            # llevar al menu principal (no se como se hace xD)
            
            return
    print("Credenciales incorrectas. Intente nuevamente.")
    login_recepcionista()
