import os
class Usuario:
    def __init__(self, rut, nombrec, correo, contra, fnac, dir, pais, ntelefno):
        self.rut = rut
        self.nombrec = nombrec
        self.correo = correo
        self.contra = contra
        self.fnac = fnac
        self.dir = dir
        self.pais = pais
        self.ntelefno = ntelefno
        # self.reserva = reserva
    
    def getRut(self):
        return self.rut
    
    def getNombrec(self):
        return self.nombrec
    
    def getContra(self):
        return self.contra
    
    def getfNac(self):
        return self.fnac
    
    def getDir(self):
        return self.dir
    
    def getPais(self):
        return self.pais
    
    def getReserva(self):
        return self.reserva
    
    def getNTelefono(self):
        return self.ntelefno
#   
class Hostal:
    def __init__(self, idhostal, nombre, direccion, habitaciones ):
        self.idhostal = idhostal
        self.nombre = nombre
        self.direccion = direccion
        self.habitaciones = habitaciones
        
    def getIdhostal(self):
        return self.idhostal
    
    def getNombre(self):
        return self.nombre
    
    def getDireccion(self):
        return self.direccion
    
    def getHabitaciones(self):
        return self.habitaciones
    

class Habitaciones:
    def __init__(self, idhabitacion, maxhab, disponibilidad, idhostal):
        self.idhabitacion = idhabitacion
        self.maxhab = maxhab
        self.disponibilidad = disponibilidad
        self.idhostal = idhostal
        
    def getIdHab(self):
        return self.idhabitacion
    
    def getMaxhab(self):
        return self.maxhab
    
    def getDispo(self):
        return self.disponibilidad
    
    def getIdHostal(self):
        return self.idhostal
    
class Recepcionista:
    def __init__(self, rut, nombre, apellido, contrasena, horario, sueldo, mail, tel, idhostal):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.contrasena = contrasena
        self.horario = horario
        self.sueldo = sueldo
        self.mail = mail
        self.tel = tel
        self.idhostal = idhostal    
        
    def getRut(self):
        return self.rut
        
    def getNombre(self):
        return self.nombre
    
    def getContrasena(self):
        return self.contrasena
    
    def getApellido(self):
        return self.apellido

    def getHorario(self):
        return self.horario
    
    def getSueldo(self):
        return self.sueldo
    
    def getMail(self):
        return self.mail
    
    def getTel(self):
        return self.tel
    
    def getIdHostal(self):
        return self.idhostal
    
    
class Reserva:
    def __init__(self, IdReserva, IdHabitacion, IdHostal, IdHuesped, IdRecepcionista, FechaLlegada, FechaSalida):
        self.IdReserva = IdReserva
        self.IdHostal = IdHostal
        self.IdHabitacion = IdHabitacion
        self.IdHuesped = IdHuesped 
        self.IdRecepcionista = IdRecepcionista
        self.FechaLlegada = FechaLlegada
        self.FechaSalida = FechaSalida

    def getIdReserva(self):
        return self.IdReserva
            
    def getIdReserva(self):
        return self.IdReserva
        
    def getIdReserva(self):
        return self.IdHabitacion

    def getIdHostal(self):
        return self.IdHostal

    def getIdHuesped(self):
        return self.IdHuesped

    def getIdRecepcionista(self):
        return self.IdRecepcionista

    def getFechaLlegada(self):
        return self.FechaLlegada

    def getFechaSalida(self):
        return self.FechaSalida



### función para borrar consola
def bconsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

