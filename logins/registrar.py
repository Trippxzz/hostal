from principal.main import bconsola
from principal.connector import Operaciones
import time
con = Operaciones
listausuarios = []

def registrar_usuario():
    mail = input("Ingrese el correo que desea utilizar: ")
    contra = input("Ingrese la contraseña: ")
    contrac = input("Confirme la contraseña: ")
    listausuarios = con.getInfoUsuario()
    for user in listausuarios:
        if mail != user.correo:
            if contra == contrac:
                print("Te has registrado correctamente, te moveremos al panel de Hostales")
                con.crearUsuario("SOLOUSER",mail, contra)
                time.sleep(2)
                bconsola()
                return 
            else:
                print("Contraseñas incorrectas")
                registrar_usuario()
                return  # Salir del bucle for cuando la contraseña sea incorrecta
        else:
             print("Este correo ya ha sido utilizado, porfavor intente con otro")
             return
            
        


    
        
        

         