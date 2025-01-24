# Libreria "tkinter" pra la interfaz grafica
import tkinter as tk

# Importamos TODOS los modulos de tkinter
from tkinter import *

from tkinter import ttk

# Indica si el registro a sido registrado o no
from tkinter import messagebox

# Importamos los clientes y la conexionApp
from Clientes import *
from ConexionApp import *


class FormularioClientes:

    # Creamos variables globales para los elementos del formulario
    global texBoxId, texBoxNombre, texBoxApellido, base, combo, groupBox, tree
    texBoxId = None
    texBoxNombre = None
    texBoxApellido = None
    base = None
    combo = None
    groupBox = None
    tree = None

    # Declaramos una funcion llamada "Formulario"


def Formulario():

    # Hay que señalar que variables globales vamos a utilizar
    global texBoxId, texBoxNombre, texBoxApellido, base, combo, groupBox, tree

    try:
        # Creamos la interfaz ----------

        # Creamos una variable "base" igual a "Tk()", que hace de referencia a la interfaz
        base = Tk()
        # Creamos la Interfaz
        base.geometry("1200x200")
        # Detallamos el titulo
        base.title("Formulario Python")

        # Rellenamos el formulario -----------

        # Creamos la variable "groupBox", que va a mostrar un panel de control. Que va a almacenar paneles mas chicos, donde habra datos personales.
        groupBox = LabelFrame(base, text="Datos del Personal", padx=5, pady=5)
        # Creamos el contenedor 1
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        # Agregamos los elementos del PRIMER CONTENEDOR -------------

        # Creamos el Label
        labelId = Label(groupBox, text="Id:", width=12, font=("arial", 12)).grid(
            row=0, column=0
        )
        # Creamos el "TexBoxId" que va a tomar los datos del usuario
        texBoxId = Entry(groupBox)
        # Asignamos la posicion en el contenedor
        texBoxId.grid(row=0, column=1)

        # Creamos el Label
        labelNombre = Label(
            groupBox, text="Nombre:", width=12, font=("arial", 12)
        ).grid(row=1, column=0)
        # Creamos el "TexBoxId" que va a tomar los datos del usuario
        texBoxNombre = Entry(groupBox)
        # Asignamos la posicion en el contenedor
        texBoxNombre.grid(row=1, column=1)

        # Creamos el Label
        labelApellido = Label(
            groupBox, text="Apellido:", width=12, font=("arial", 12)
        ).grid(row=2, column=0)
        # Creamos el "TexBoxId" que va a tomar los datos del usuario
        texBoxApellido = Entry(groupBox)
        # Asignamos la posicion en el contenedor
        texBoxApellido.grid(row=2, column=1)

        # Agreamos el selector de sexo
        labelSexo = Label(groupBox, text="Sexo:", width=12, font=("arial", 12)).grid(
            row=3, column=0
        )
        # Se guarda como una variable de cadena de texto.
        seleccionSexo = tk.StringVar()
        # Creamos el comboBox
        combo = ttk.Combobox(
            groupBox, values=["Masculino", "Femenino"], textvariable=seleccionSexo
        )
        # Declaramos el lugar que va a ocupar en el contenedor
        combo.grid(row=3, column=1)
        # Declaramos un texto por defecto
        seleccionSexo.set("Seleccionar")

        # Creamos los botones
        Button(groupBox, text="Guardar", width=10, command=guardarRegistros).grid(
            row=4, column=0
        )
        Button(groupBox, text="Modificar", width=10, command=modificarRegistros).grid(
            row=4, column=1
        )
        Button(groupBox, text="Eliminar", width=10, command=eliminarRegistros).grid(
            row=4, column=2
        )

        # Agregamos los elementos del SEGUNDO CONTENEDOR -------------

        # Creamos otro Label para el segundo contenedor
        groupBox = LabelFrame(
            base,
            text="Lista del Personal",
            padx=5,
            pady=5,
        )
        # Posicionamos el contenedor
        groupBox.grid(row=0, column=1)

        # Creamos un Treeview

        # Configuramos las columnas
        tree = ttk.Treeview(
            groupBox,
            columns=("Id", "Nombres", "Apellidos", "Sexo"),
            show="headings",
            height=5,
        )
        # Asignamos los valores a las columnas ------------------

        # Columna ID
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Id")

        # Columna Nombre
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Nombre")

        # Columna Apellido
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Apellido")

        # Columna Sexo
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Sexo")

        # Agregar los datos a la tabla
        # Mostrar la tabla

        # Mostramos los clientes en la tabla -----------------------------
        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)

        # Ejecutamos la funcion hacer click y mostrar el resultado en los Entry--------------------------
        tree.bind("<<TreeviewSelect>>", seleccionarRegistro)

        # Nos permite que funcione La columna 2
        tree.pack()

        # Ceramos la interfaz
        base.mainloop()

    except ValueError as error:
        print("Error al mostrar la interfaz,error: {}".format(error))


def guardarRegistros():

    global texBoxNombre, texBoxApellido, combo, groupBox

    try:

        # Verificar si los widgets estan inicializados
        if texBoxNombre is None or texBoxApellido is None or combo is None:
            print("Los widgets no estan inicializados")
            return
        # Si estan inicializados creamos variables que van a almacenar lo que vamos a ingresar por la interfaz
        nombres = texBoxNombre.get()
        apellidos = texBoxApellido.get()
        sexo = combo.get()

        # Llamamos a la clase "CClientes" y a la funcion "IngresarClientes"
        CClientes.IngresarClientes(nombres, apellidos, sexo)
        messagebox.showinfo("Informacion", "Los datos fueron guardados")

        # Llamamos a la funcion actualizarTreeView(), para actualizar, modificar, elminar
        actualizarTreeView()

        # Limpiamos los campos
        texBoxNombre.delete(0, END)
        texBoxApellido.delete(0, END)

    except ValueError as error:
        print("Error al guardar los datos {}".format(error))


def actualizarTreeView():
    global tree

    try:
        # Borramos todos los elementos actuales del TreeView
        # El metodo get_children, entonces me vacia todo menos las cabeceras/padres
        tree.delete(*tree.get_children())

        # Obtener los nuevos datos a mostrar
        datos = CClientes.mostrarClientes()

        # Insertamos los nuevos datos en el TreeView
        # Mostramos los clientes en la tabla
        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)
    except ValueError as error:
        print("Error al actualizar los datos de la tabla {}".format(error))


def seleccionarRegistro(event):
    try:
        # Obtener el Id del elemento seleccionado
        itemSeleccionado = tree.focus()

        # Realizamos al comparacion
        if itemSeleccionado:
            # Obtener los valores por columna y los guardamos
            values = tree.item(itemSeleccionado)["values"]

            # Establecemos los valores en los widgets "Entry" ----------

            # Eliminamos el valor ID
            texBoxId.delete(0, END)
            # Insertamos el nuevo valor ID
            texBoxId.insert(0, values[0])
            # Eliminamos el valor Nombre
            texBoxNombre.delete(0, END)
            # Insertamos el nuevo valor Nombre
            texBoxNombre.insert(0, values[1])
            # Eliminamos el valor Apellido
            texBoxApellido.delete(0, END)
            # Insertamos el nuevo valor Apellido
            texBoxApellido.insert(0, values[2])
            # Cambiamos el valor del Sexo
            combo.set(values[3])

    except ValueError as error:
        print("Error al seleccionar registro {}".format(error))


def modificarRegistros():

    global texBoxId, texBoxNombre, texBoxApellido, combo, groupBox

    try:

        # Verificar si los widgets estan inicializados
        if (
            texBoxId is None
            or texBoxNombre is None
            or texBoxApellido is None
            or combo is None
        ):
            print("Los widgets no estan inicializados")
            return
        # Si estan inicializados creamos variables que van a almacenar lo que vamos a ingresar por la interfaz
        idUsuario = texBoxId.get()
        nombres = texBoxNombre.get()
        apellidos = texBoxApellido.get()
        sexo = combo.get()

        # Llamamos a la clase "CClientes" y a la funcion "IngresarClientes"
        CClientes.modificarClientes(idUsuario, nombres, apellidos, sexo)
        messagebox.showinfo("Informacion", "Los datos fueron guardados")

        # Llamamos a la funcion actualizarTreeView(), para actualizar, modificar, elminar
        actualizarTreeView()

        # Limpiamos los campos
        texBoxId.delete(0, END)
        texBoxNombre.delete(0, END)
        texBoxApellido.delete(0, END)

    except ValueError as error:
        print("Error al modificar los datos {}".format(error))


def eliminarRegistros():

    global texBoxId, texBoxNombre, texBoxApellido

    try:

        # Verificar si los widgets estan inicializados
        if texBoxId is None:
            print("Los widgets no estan inicializados")
            return

        # Si estan inicializados creamos variables que van a almacenar lo que vamos a ingresar por la interfaz
        idUsuario = texBoxId.get()

        # Llamamos a la clase "CClientes" y a la funcion "IngresarClientes"
        CClientes.eliminarClientes(idUsuario)
        messagebox.showinfo("Informacion", "Los datos fueron eliminados")

        # Llamamos a la funcion actualizarTreeView(), para actualizar, modificar, elminar
        actualizarTreeView()

        # Limpiamos los campos
        texBoxId.delete(0, END)
        texBoxNombre.delete(0, END)
        texBoxApellido.delete(0, END)

    except ValueError as error:
        print("Error al eliminar los datos {}".format(error))


Formulario()
