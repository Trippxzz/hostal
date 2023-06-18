from logins.sesion import iniciar_sesion
from logins.registrar import registrar_usuario

# print("Bienvenid@s a Hostal XXXX")
# seleccionar:str =  input("1) Para Iniciar Sesión/Registrarse \n2) Para ver hostales \n3) Para iniciar sesión como trabajador\n")

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
    

# def menuPrincipalIn():
#     print("==================== MENÚ PRINCIPAL HOSTALES  ====================")
#     print("========================= SESION INICIADA ========================")
#     print("1.- Ver hostales")
#     print("2.- Iniciar sesion como trabajador")
#     print("3.- Salir")
#     print("========================================================")
#     seleccionar = int(input("Seleccione una opción: "))
#     if seleccionar == 1:
#         print("a")
    
# def menuHostales():
#     print("==================== HOSTALES ====================")
#     print("1.- Hostal Puerto Montt")
#     print("2.- Hostal Iquique")
#     print("3.- Hostal Valdivia")
#     print("4.- Hostal Coquimbo")
#     print("5.- Hostal Arica")
#     print("6.- Regresar al Menu Principal")
#     print("==================================================")
#     seleccionar = int(input("Seleccione una opción: "))    
    if seleccionar == 1:
        iniciar_sesion()



MenuPrincipal()


        
        