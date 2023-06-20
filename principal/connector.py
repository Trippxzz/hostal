import pymysql
from principal.main import Usuario, Recepcionista, Hostal, Habitaciones


class Operaciones:
    def getInfoUsuario():
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute( "SELECT * FROM cliente" )
        lista = []
        for rut, nombre, correo, contra, fnac, dir, pais, ntelefono in cur:
            op1 = Usuario(rut, nombre, correo,contra, fnac, dir, pais, ntelefono)
            lista.append(op1)
        cur.close()
        cone.close()
        return lista
    
    def getCorreoRegister(cor):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute("""SELECT * FROM cliente WHERE Correo = %s """,(cor,))
        lista = []
        for rut, nombre, correo, contra, fnac, dir, pais, ntelefono in cur:
            op6 = Usuario(rut, nombre, correo, contra, fnac, dir, pais, ntelefono)
            lista.append(op6)
        cur.close()
        cone.close()
        return lista 
    
    def getRut(cor):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute("""SELECT * FROM cliente WHERE Correo = %s """,(cor,))
        lista = []
        for rut, nombre, correo, contra, fnac, dir, pais, ntelefono in cur:
            op6 = Usuario(rut, nombre, correo, contra, fnac, dir, pais, ntelefono)
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
    
    def getInfoTrabajadorC(c):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute( "SELECT * FROM Recepcionista WHERE Gmail = %s """, (c,) )
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
        
    def actualizar_a_cliente(rut, nombre, correo, contra, fnac, dire, p, ntelefno):
        cone = pymysql.connect(host='localhost', user='root', passwd='', db='hostal')
        cur = cone.cursor()
        sql = """UPDATE cliente SET RUT = %s, Nombre = %s, Contrasena = %s, Nacimiento = %s, Direccion = %s, Pais = %s, NTelefono = %s WHERE Correo = %s"""
        values = (rut, nombre, contra, fnac, dire, p,ntelefno, correo)
        cur.execute(sql, values)
        cone.commit()        
        cur.close()
        cone.close()

    
    def crear_reservas(IdReserva, IdHostal, IdHabitacion, IdHuesped, IdRecepcionista, FechaLlegada, FechaSalida):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute("""INSERT INTO reserva (IdReserva, IdHostal, IdHabitacion, IdHuesped, IdRecepcionista, FechaLlegada, FechaSalida) VALUES (%s,%s, %s,%s,%s, %s,%s)
                   """,(IdReserva, IdHostal, IdHabitacion, IdHuesped, IdRecepcionista, FechaLlegada, FechaSalida))
        cone.commit()
        cur.close()
        cone.close()

    def actualizar_disponibilidad(canthab, disponibilidad, idh):
        cone = pymysql.connect(host='localhost', user='root', passwd='', db='hostal')
        cur = cone.cursor()  
        sql = """UPDATE habitacion SET MaxHab = %s, Disponibilidad = %s WHERE IdHostal = %s"""
        values = (canthab, disponibilidad, idh)    
        cur.execute(sql, values)
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

    def genregPago(ide,monto,mpago ,factual):
        cone = pymysql.connect( host='localhost', user= 'root', passwd='', db='hostal' )
        cur = cone.cursor()
        cur.execute("""INSERT INTO pago (Ntransaccion, Monto, Metodo, FechaDePago) VALUES (%s,%s, %s,%s)
                   """,(ide,monto,mpago ,factual))
        cone.commit()
        cur.close()
        cone.close()