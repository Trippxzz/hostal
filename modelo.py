class departamento:
    
    def __init__ (self , idDept,nombreDept):
        self.idDept = idDept
        self.nombreDept = nombreDept

    def __str__ ( self ):
        # Retornamos el nombre de la persona
        return self.nombreDept
    
    def getIdDept(self):
        return self.idDept
    
    def getNombreDept(self):
        return self.nombreDept
    
    def setIdDept(self,idDept):
        self.idDept  =idDept    

    def setNombreDept(self,nombreDept):
        self.nombreDept  =nombreDept  
           
    
class empleado:
    def __init__ (self , 
                  idEmpleado,
                  nombreEmpleado,
                  apellidoMaterno,
                  apellidoPaterno,
                  email,
                  numeroTelefono,
                  fechaContratacion,
                  fechaNacimiento,
                  idCargo,
                  salario,
                  comission,
                  idJefe,
                  iddepartamento,
                  direccion,
                  ):
        self.idEmpleado = idEmpleado
        self.nombreEmpleado = nombreEmpleado
        self.apellidoMaterno = apellidoMaterno
        self.apellidoPaterno = apellidoPaterno
        self.email = email
        self.numeroTelefono = numeroTelefono
        self.fechaContratacion = fechaContratacion
        self.fechaNacimiento = fechaNacimiento
        self.idCargo = idCargo
        self.salario = salario
        self.comission = comission
        self.idJefe = idJefe
        self.iddepartamento = iddepartamento
        self.direccion = direccion

    def __str__ ( self ):
        # Retornamos el nombre de la persona
        return self.nombreEmpleado
    
    def getIdEmpleado(self):
        return self.idEmpleado
    
    def getNombreEmpleado(self):
        return self.nombreEmpleado
 
    def getApellidoMaterno(self):
        return self.apellidoMaterno
    
    def getApellidoPaterno(self):
        return self.apellidoPaterno
    
    def getEmail(self):
        return self.email      

    def getNumeroTelefono(self):
        return self.numeroTelefono     
     
    def getFechaContratacion(self):
        return self.fechaContratacion   

    def getFechaNacimiento(self):
        return self.fechaNacimiento    

    def getIdCargo(self):
        return self.idCargo    

    def getSalario(self):
        return self.salario    

    def getComission(self):
        return self.comission           
       
    def getIdJefe(self):
        return self.idJefe          

    def getIddepartamento(self):
        return self.iddepartamento    

    def getDireccion(self):
        return self.direccion     

##seters
    def setIdEmpleado(self,idEmpleado):
        self.idEmpleado=idEmpleado
    
    def setNombreEmpleado(self,nombreEmpleado):
        self.nombreEmpleado=nombreEmpleado
 
    def setApellidoMaterno(self,apellidoMaterno):
        self.apellidoMaterno=apellidoMaterno
    
    def setApellidoPaterno(self,apellidoPaterno):
        self.apellidoPaterno=apellidoPaterno
    
    def setEmail(self,email):
        self.email  =email    

    def setNumeroTelefono(self,numeroTelefono):
        self.numeroTelefono =numeroTelefono    
     
    def setFechaContratacion(self,fechaContratacion):
        self.fechaContratacion =fechaContratacion   

    def setFechaNacimiento(self,fechaNacimiento):
        self.fechaNacimiento =fechaNacimiento   

    def setIdCargo(self,idCargo):
        self.idCargo =idCargo    

    def setSalario(self,salario):
        self.salario =salario 

    def setComission(self,comission):
        self.comission =comission         
       
    def setIdJefe(self,idJefe):
        self.idJefe= idJefe        

    def setIddepartamento(self,iddepartamento):
        self.iddepartamento =iddepartamento  

    def setDireccion(self,direccion):
        self.direccion = direccion
