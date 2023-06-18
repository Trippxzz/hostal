from logins.sesion import iniciar_sesion
from logins.registrar import registrar_usuario
from logins.recepcionistas import login_recepcionista
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
        iniciar_sesion()
    elif seleccionar == 2:
        registrar_usuario()
    # elif seleccionar == 3:
    #     registrar_usuario()
    elif seleccionar == 4:
        login_recepcionista()
    

MenuPrincipal()


        
        