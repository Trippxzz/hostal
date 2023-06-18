import pymysql
from main import Usuario, Recepcionista


class Operaciones:
    def getInfoUsuario(self):
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

    def getInfoTrabajador(self):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute( "SELECT * FROM Recepcionista" )
        lista = []
        for rut, nombre, correo, contra, fnac, dir, pais in cur:
            op2 = Recepcionista(rut, nombre, correo,contra, fnac, dir, pais)
            lista.append(op2)
        cur.close()
        cone.close()
        return lista
        
    def crearUsuario(self, correo, contra):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute("""INSERT INTO cliente (correo, contrasena) VALUES (:0,:1) """,(correo,contra))
        cone.commit()
        cur.close()
        cone.close()
    

    