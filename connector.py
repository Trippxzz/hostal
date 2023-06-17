import pymysql
from main import Usuario
cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='Hostal' )
cur = cone.cursor()



class Operaciones:
    def getInfoUsuario(self):
        cur.execute( "SELECT * FROM cliente" )
        lista = []
        for rut, nombre, contra, fnac, dir, pais, reserva in cur:
            op1 = Usuario(rut, nombre, contra, fnac, dir, pais, reserva)
            lista.append(op1)
        cur.close()
        cone.close()
        return lista
    