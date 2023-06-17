import cx_Oracle

from modelo import departamento

class operacion:
    
    """obtenerDepartamentos
    permite obtener el listado de todos los departamentos existentes en la tabla
    
    """
    def obtenerDepartamentos(self):
        connection = cx_Oracle.connect(
                    user="tallerfun",
                    password="123",
                    dsn="localhost/xe")
        cursor = connection.cursor()
        cursor.execute('SELECT ID_DEPARTMENTO, NOMBRE_DEPARTAMENTO FROM TALLERFUN.DEPARTAMENTOS')
        lista=[]
        for id, nombreDept in cursor:
            p1=departamento(id,nombreDept)
            lista.append(p1)
            #print("kk:", id, nombreDept)
        cursor.close()
        connection.close()
        return lista
    
    def obtenerDepartamento(self, idDept):
        connection = cx_Oracle.connect(
                    user="tallerfun",
                    password="123",
                    dsn="localhost/xe")
        cursor = connection.cursor()
        cursor.execute("""SELECT ID_DEPARTMENTO, NOMBRE_DEPARTAMENTO 
                          FROM TALLERFUN.DEPARTAMENTOS 
                          WHERE ID_DEPARTMENTO =: ID """,
                          ID=idDept
                       )
        lista=[]
        for id, nombreDept in cursor:
            p1=departamento(id,nombreDept)
            lista.append(p1)
            #print("Values:", id, nombreDept)
        cursor.close()
        connection.close()
        return lista

    def obtenerDepartamento2(self, idDept):
        connection = cx_Oracle.connect(
                    user="tallerfun",
                    password="123",
                    dsn="localhost/xe")
        cursor = connection.cursor()
        cursor.execute("""SELECT ID_DEPARTMENTO, NOMBRE_DEPARTAMENTO 
                       FROM TALLERFUN.DEPARTAMENTOS
                       WHERE ID_DEPARTMENTO=:0""",(idDept,))
        lista=[]
        for id, nombreDept in cursor:
            p1=departamento(id,nombreDept)
            lista.append(p1)
            #print("Values:", id, nombreDept)
        cursor.close()
        connection.close()
        return lista
    
    def agregarDepartamento(self,idDept,nombreDept):
        connection = cx_Oracle.connect(
                    user="tallerfun",
                    password="123",
                    dsn="localhost/xe")
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO DEPARTAMENTOS 
                          (ID_DEPARTMENTO, NOMBRE_DEPARTAMENTO) 
                           VALUES (:0,:1) """,
                          (idDept,nombreDept)
                       )
        

        connection.commit()
        cursor.close()
        connection.close()

    def eliminarDepartamento(self,idDept):
        connection = cx_Oracle.connect(
                    user="tallerfun",
                    password="123",
                    dsn="localhost/xe")
        cursor = connection.cursor()
        cursor.execute("""DELETE FROM DEPARTAMENTOS 
                          WHERE ID_DEPARTMENTO =:0 """
                          ,
                          (idDept,)
                       )
        

        connection.commit()
        cursor.close()
        connection.close()

    def actualizarDepartamento(self,idDept,nombreDept):
        connection = cx_Oracle.connect(
                    user="tallerfun",
                    password="123",
                    dsn="localhost/xe")
        cursor = connection.cursor()
        cursor.execute("""UPDATE DEPARTAMENTOS 
                          SET NOMBRE_DEPARTAMENTO =:0 
                          WHERE ID_DEPARTMENTO =:1"""
                          ,
                          (nombreDept,idDept)
                       )
        

        connection.commit()
        cursor.close()
        connection.close()