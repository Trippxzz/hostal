class Usuario:
    def __init__(self,rut, nombrec, contrasena, fnac, dir, pais, reserva):
        self.rut = rut
        self.nombrec = nombrec
        self.contrasena = contrasena
        self.fnac = fnac
        self.dir = dir
        self.pais = pais
        self.reserva = reserva
    
    def getRut(self):
        return self.rut
    
    def getNombrec(self):
        return self.nombrec
    
    def getContrasena(self):
        return self.contrasena
    
    def getfNac(self):
        return self.fnac
    
    def getDir(self):
        return self.dir
    
    def getPais(self):
        return self.pais
    
    def getReserva(self):
        return self.reserva
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
    def __init__(self, idhabitacion, maxhab, dispoibilidad):
        self.idhabitacion = idhabitacion
        self.maxhab = maxhab
        self.disponibilidad = dispoibilidad
        
    def getIdHab(self):
        return self.idhabitacion
    
    def getMaxhab(self):
        return self.maxhab
    
    def getDispo(self):
        return self.disponibilidad
    
class Recepcionista:
    def __init__(self, rut, nombrec, horario, sueldo, mail, tel, idhostal):
        self.rut = rut
        self.nombrec = nombrec
        self.horario = horario
        self.sueldo = sueldo
        self.mail = mail
        self.tel = tel
        self.idhostal = idhostal    
        
    def getRut(self):
        return self.rut
        
    def getNombrec(self):
        return self.nombrec
    
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
    
    
        