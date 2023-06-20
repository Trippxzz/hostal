from logins.sesion import iniciar_sesion
from logins.registrar import registrar_usuario
from logins.recepcionistas import login_recepcionista
from reservas.hacerreserva import menuHostales
cis = None ## c: Como | i: Inicio | s: Sesion
n = None #Tomará el valor de correo, (Para hacer condiciones al momento de hacer reservas)

def MenuPrincipal():
    print("=============== MENÚ PRINCIPAL HOSTALES ================")
    print("1.- Iniciar sesion usuario")
    print("2.- Registrar usuario")
    print("3.- Ver hostales")
    print("4.- Iniciar sesion como trabajador")
    print("5.- Salir")
    print("========================================================")
    
    seleccionar = int(input("Seleccione una opción: "))    
    if seleccionar == 1:
        iniciar_sesion(cis, n)
    elif seleccionar == 2:
        registrar_usuario(cis, n)
    elif seleccionar == 3:
        menuHostales(cis, n)
    elif seleccionar == 4:
        login_recepcionista(cis, n)
    elif seleccionar == 5:
        exit()
    
MenuPrincipal()


        
        