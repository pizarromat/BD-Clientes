# Importamos todos lo que contiene ConexionApp.py
from ConexionApp import *


class CClientes:

    # Creamos la funcion crear clientes
    def mostrarClientes():
        try:
            # Creamos una variable a la cual se le asigna la clase "CConexion", que contiene la funcion "ConexionBaseDeDatos()"
            conect = CConexion.ConexionBaseDeDatos()
            # Creamos una variable que va a ejecutar la conexion que tenemos
            cursor = conect.cursor()
            # el cursor va a ejecutar la siguiente linea de MySQL
            cursor.execute("select * from usuarios;")
            # La variable va a ser igual a cursor.fetchall() para mostrar todos los resultados
            miResultado = cursor.fetchall()
            # Commit
            conect.commit()
            # Cerramos la conexion
            conect.close()
            # Devolvemos los datos
            return miResultado

        except mysql.connector.Error as error:
            print("Error de muestreo de datos {}".format(error))

    # Creamos la funcion Ingresar Clientes
    def IngresarClientes(nombre, apellido, sexo):

        try:

            # Creamos una variable a la cual se le asigna la clase "CConexion", que contiene la funcion "ConexionBaseDeDatos()"
            conect = CConexion.ConexionBaseDeDatos()
            # Creamos una variable que va a ejecutar la conexion que tenemos
            cursor = conect.cursor()
            # Creamos una variable que vamos a ingresar la consulta a MySQL
            sql = "insert into usuarios values(null, %s, %s, %s);"
            # La variable valores tiene que ser una tupla
            # Como minima expresion es: (valor,) La "coma" hace que sea una tupla
            # Las tuplas son listas inmutables, eso significa que no se puede modificar.
            valores = (nombre, apellido, sexo)
            # Esta variable une la consulta con los valores
            cursor.execute(sql, valores)
            # Commit
            conect.commit()
            # Si funciona que muestre un mensaje
            print(cursor.rowcount, "Registro ingresado")
            # Cerramos la conexion
            conect.close()

        except mysql.connector.Error as error:
            print("Error de ingresos de datos {}".format(error))

    # Creamos la funcion Modificar Clientes
    def modificarClientes(idUsuario, nombre, apellido, sexo):

        try:

            # Creamos una variable a la cual se le asigna la clase "CConexion", que contiene la funcion "ConexionBaseDeDatos()"
            conect = CConexion.ConexionBaseDeDatos()
            # Creamos una variable que va a ejecutar la conexion que tenemos
            cursor = conect.cursor()
            # Creamos una variable que vamos a ingresar la consulta a MySQL
            sql = "UPDATE usuarios SET usuarios.nombre = %s,usuarios.apellido = %s,usuarios.sexo = %s Where usuarios.id = %s;"
            # La variable valores tiene que ser una tupla
            # Como minima expresion es: (valor,) La "coma" hace que sea una tupla
            # Las tuplas son listas inmutables, eso significa que no se puede modificar.
            valores = (nombre, apellido, sexo, idUsuario)
            # Esta variable une la consulta con los valores
            cursor.execute(sql, valores)
            # Commit
            conect.commit()
            # Si funciona que muestre un mensaje
            print(cursor.rowcount, "Registro ingresado")
            # Cerramos la conexion
            conect.close()

        except mysql.connector.Error as error:
            print("Error al modificar los datos {}".format(error))

    # Creamos la funcion Modificar Clientes
    def eliminarClientes(idUsuario):

        try:

            # Creamos una variable a la cual se le asigna la clase "CConexion", que contiene la funcion "ConexionBaseDeDatos()"
            conect = CConexion.ConexionBaseDeDatos()
            # Creamos una variable que va a ejecutar la conexion que tenemos
            cursor = conect.cursor()
            # Creamos una variable que vamos a ingresar la consulta a MySQL
            sql = "DELETE from usuarios WHERE usuarios.id=%s;"
            # La variable valores tiene que ser una tupla
            # Como minima expresion es: (valor,) La "coma" hace que sea una tupla
            # Las tuplas son listas inmutables, eso significa que no se puede modificar.
            valores = (idUsuario,)
            # Esta variable une la consulta con los valores
            cursor.execute(sql, valores)
            # Commit
            conect.commit()
            # Si funciona que muestre un mensaje
            print(cursor.rowcount, "Registro ingresado")
            # Cerramos la conexion
            conect.close()

        except mysql.connector.Error as error:
            print("Error al Eliminar los datos {}".format(error))
