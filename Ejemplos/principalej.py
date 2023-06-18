import operaciones
import principal.modelo as modelo

op=operaciones.operacion()

listax=[]
listax= op.obtenerDepartamentos()

for reg in listax:
    print("Values:", reg.idDept, reg.nombreDept)


#lista2=[]
#lista2= op.obtenerDepartamento(100)

#for reg in lista2:
#    print("Values:", reg.idDept, reg.nombreDept)
    
lista2=[]
op.agregarDepartamento(1,"dep_tere")
lista2= op.obtenerDepartamento2(3)

for reg in lista2:
    print("Values:", reg.idDept, reg.nombreDept)
    

lista3=[]
op.actualizarDepartamento(3,"dep_tere2")

lista3= op.obtenerDepartamento2(3)

for reg in lista3:
    print("Values:", reg.idDept, reg.nombreDept)
    
op.eliminarDepartamento(4)