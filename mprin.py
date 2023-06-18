from principal import connector
from sesiones import iniciar_sesion
import time
hostales = []
con =connector.Operaciones()
listausuarios = []

# print("Bienvenid@s a Hostal XXXX")
# seleccionar:str =  input("1) Para Iniciar Sesión/Registrarse \n2) Para ver hostales \n3) Para iniciar sesión como trabajador\n")

def MenuPrincipal():
    print("==================== MENÚ PRINCIPAL HOSTALES ====================")
    print("1.- Iniciar sesion usuario")
    print("2.- Registrar usuario")
    print("3.- Ver hostales")
    print("4.- Iniciar sesion como trabajador")
    print("5.- Salir")
    print("========================================================")
    seleccionar = int(input("Seleccione una opción: "))

def menuPrincipalIn():
    print("==================== MENÚ PRINCIPAL HOSTALES  ====================")
    print("========================= SESION INICIADA ========================")
    print("1.- Ver hostales")
    print("2.- Iniciar sesion como trabajador")
    print("3.- Salir")
    print("========================================================")
    seleccionar2 = int(input("Seleccione una opción: "))
    

if seleccionar == 1:
    iniciar_sesion()





        
        