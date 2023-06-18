--Administrador--
from persona import Persona
class Administrador(Persona):
    def __init__(self, claveAdministrador=int, rut="", clave="", nombre="", cargo=""):
        super().__init__(rut, clave, nombre, cargo)
        self.__claveAdministrador = claveAdministrador
    def __str__(self):
        return f"{super().__str__()} claveAdministrador: {self.__claveAdministrador}"

--empleado--
from pickle import TRUE
from persona import Persona
class Empleado(Persona):
    __listaEmpleados= []
    def __init__(self, rut="", clave="", nombre="", cargo="", depto=""):
        super().__init__(rut, clave, nombre, cargo)
        self.__depto= depto
    def __str__(self):
        return f"{super().__str__()} depto: {self.__depto}"
    def getRut(self):
        return super().getRut()
    def addEmpleado(self, rut, clave, nombre, cargo, depto):
        if len(self.__listaEmpleados >0):
            for em in self.__listaEmpleados: 
                if rut not in em.getRut():
                    self.__listaEmpleados.append(Empleado(rut, clave, nombre, cargo, depto))
                    return "empleado registrado de manera exitosa" 
                return "empleado ya existe no puede volver a ingresarlo"
        else:
            return "empleado registrado de manera exitosa"

--Persona--
class Persona:
    def __init__(self,rut="",clave="",nombre="",cargo=""):
        self.__rut= rut
        self.__clave= clave
        self.__nombre= nombre
        self.__cargo= cargo
    def __str__(self):
        return f"rut: {self.__rut} clave: {self.__clave} nombre: {self.__nombre} cargo: {self.__cargo}"
    def getRut(self):
        return self.__rut

--main--
from empleado import Empleado
--opcion 1 del sub menú--
emp = Empleado("", "", "", "", "")
if op ==1:
    rut  = input("Ingrese su rut")
    clave = input
    print(emp.addEmpleado(rut, clave, nombre, cargo, depto))