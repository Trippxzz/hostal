import pymysql
from principal.main import Usuario, Recepcionista


class Operaciones:
    def getInfoUsuario():
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute( "SELECT * FROM cliente" )
        lista = []
        for rut, nombre, correo, contra, fnac, dir, pais in cur:
            op1 = Usuario(rut, nombre, correo,contra, fnac, dir, pais)
            lista.append(op1)
        cur.close()
        cone.close()
        return lista

    def getInfoTrabajador():
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute( "SELECT * FROM Recepcionista" )
        lista = []
        for rut, nombre, apellido, contrasena, horario, sueldo, mail, tel, idhostal in cur:
            op2 = Recepcionista(rut, nombre, apellido, contrasena, horario, sueldo, mail, tel, idhostal)
            lista.append(op2)
        cur.close()
        cone.close()
        return lista
        
    def crearUsuario(rut, correo, contra):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute("""INSERT INTO cliente (RUT, Correo, Contra) VALUES (%s,%s, %s) """,(rut, correo,contra))
        cone.commit()
        cur.close()
        cone.close()
    

    