# Instalamos mysql-connector
# pip install  mysql-connector-python

# Importamos la base de datos "mysql.connector"
import mysql.connector


# Creamos una clase Conexion
class CConexion:
    # Creamso una funcion de conexion
    def ConexionBaseDeDatos():
        # Creamos el prueba y error por si no funciona la conexion a la base de datos
        try:

            # Creamos una variable llamada "conexion", le decimos que la conexion es de "mysql.connector.connect(usuario,contraseña,host,base de datos,puerto)"
            conexion = mysql.connector.connect(
                user="root",
                password="root",
                host="localhost",
                database="clientes",
                port="3306",
            )

            # Imprimimos si funciono la conexion
            print("Conexion correcta")

            # Rotornamos la variable conexion, porque cuando voy a ingresar, eliminar, agregar datos, entonces vamos a utilizar la conexion.
            return conexion

        except mysql.connector.Error as error:
            print("Error al conectarme a la base de datos {}".format(error))

            return conexion

    ConexionBaseDeDatos()
