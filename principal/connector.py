import pymysql
from principal.main import Usuario, Recepcionista, Hostal, Habitaciones


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
    
    def getRut(cor):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute("""SELECT * FROM cliente WHERE Correo = %s """,(cor,))
        lista = []
        for rut, nombre, correo, contra, fnac, dir, pais in cur:
            op6 = Usuario(rut, nombre, correo, contra, fnac, dir, pais)
            lista.append(op6)
        cur.close()
        cone.close()
        return lista

    def getInfoTrabajador():
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute( "SELECT * FROM Recepcionista" )
        lista = []
        for rut, nombre, apellido, contra, horario, sueldo, mail, tel, idhostal in cur:
            op2 = Recepcionista(rut, nombre, apellido, contra, horario, sueldo, mail, tel, idhostal)
            lista.append(op2)
        cur.close()
        cone.close()
        return lista
        
    def crearUsuario(rut, correo, contra):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute("""INSERT INTO cliente (RUT, Correo, Contrasena) VALUES (%s,%s, %s) """,(rut, correo,contra))
        cone.commit()
        cur.close()
        cone.close()
        
    def actualizar_a_cliente(rut, nombre, correo, contra, fnac, dire, p):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute("""UPDATE  cliente SET (RUT, Correo, Contrasena, Nacimiento, Direccion, Pais ) VALUES (%s,%s, %s, %s,%s, %s, %s) """,(rut, nombre, correo, contra, fnac, dire, p))
        cone.commit()
        cur.close()
        cone.close()       
    
    def crear_reservas(IdReserva, IdHostal, IdHabitacion, IdHuesped, IdRecepcionista, FechaLlegada, FechaSalida):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute("""INSERT INTO reservas (IdReserva, IdHostal, IdHabitacion, IdHuesped, IdRecepcionista, FechaLlegada, FechaSalida) VALUES (%s,%s, %s,%s,%s, %s,%s)
                   """,(IdReserva, IdHostal, IdHabitacion, IdHuesped, IdRecepcionista, FechaLlegada, FechaSalida))
        cone.commit()
        cur.close()
        cone.close()
        

    def mostrar_reservas():       
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute( "SELECT * FROM reserva" )
        lista = []
        for rut, nombre, apellido, contra, horario, sueldo, mail, tel, idhostal in cur:
            op3 = Recepcionista(rut, nombre, apellido, contra, horario, sueldo, mail, tel, idhostal)
            lista.append(op3)
        cur.close()
        cone.close()
        return lista
    
    def getHostales():
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute( "SELECT * FROM Hostal" )
        lista = []
        for idhostal, nombre, direccion, ingresos in cur:
            op4 = Hostal(idhostal, nombre, direccion, ingresos)
            lista.append(op4)
        cur.close()
        cone.close()
        return lista
    
    def getHabitaciones(idhostal):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute("""SELECT * FROM Habitacion WHERE IdHostal = %s """,(idhostal,))
        lista = []
        for idhabitacion, maxhab, disponibilidad, idhostal in cur:
            op5 = Habitaciones(idhabitacion, maxhab, disponibilidad, idhostal)
            lista.append(op5)
        cur.close()
        cone.close()
        return lista