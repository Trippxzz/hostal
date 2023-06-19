from principal.main import bconsola
from principal.connector import Operaciones
from reservas.hacerreserva import menuHostales
import time, string, secrets


con = Operaciones
listausuarios = []

def registrar_usuario(cis, n):
    bconsola()
    print("=============== Registrate ================")
    mail = input("Ingrese el correo que desea utilizar: ")
    listausuarios = con.getCorreoRegister(mail)
    if not listausuarios:  
        contra = input("Ingrese la contraseña: ")
        contrac = input("Confirme la contraseña: ")
        if contra == contrac:
            cis = "Usuario"
            print("Te has registrado correctamente, te moveremos al panel de Hostales")
            con.crearUsuario(generar_id(), mail, contra)
            time.sleep(3)
            bconsola()
            n = mail
            menuHostales(cis, n)
            return
        else:
            print("Las contraseñas no coinciden")
            registrar_usuario()
            return
    else:
        print("Este correo ya ha sido utilizado, por favor intente con otro")
        time.sleep(2)
        registrar_usuario()
        return
            
        
def generar_id():
    caracteres = string.ascii_lowercase + string.digits
    id_random = ''.join(secrets.choice(caracteres) for _ in range(4))
    return "SUSER-" + id_random ##SUSER SIGNIFICA SOLO USER/USUARIO | ES DECIR, AUN NO HA REALIZADO NINGUNA COMPRA
        
        

         