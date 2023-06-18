from principal import main, connector 

def registrar_usuario():
    intentos = 0

    nombrec = input("Ingrese el nombre: ")
    correo = input("Ingrese el correo: ")
    contra = input("Ingrese la contraseña: ")

    for user in listausuarios:
        if correo == user.correo:
            print("Este correo ya esta registrado")
            return 
        
    while intentos < 3:
        contraseña = input("Ingrese la contraseña: ")
        confirmar_contraseña = input("Confirmne la contraseña")

        if contraseña == confirmar_contraseña:
            usuario = Usuario(nombrec, correo, contraseña)

        con.insertarUsuario(usuario) #insertar usuario en la base de datos

        print("Usuario registrado ")
        return
    else:
        print("las contraseñas no coinciden")
         intentos += 1
        
        

         