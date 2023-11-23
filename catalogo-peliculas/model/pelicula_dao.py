from .conexion_db import *
from tkinter import messagebox
def crear_tabla():
    conexion = ConexionDB()

    sql ='''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR,
        Genero VARCHAR,
        Calificacion VARCHAR,
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    ''' 
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Crear Registro"
        mensaje = "se creo la tabla en la base de datos"
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = "Crear Registro"
        mensaje = "La tabla ya esta creada"
        messagebox.showwarning(titulo,mensaje)

def borar_tabla():
    conexion = ConexionDB()
    sql = "DROP TABLE peliculas"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Borrar Registro"
        mensaje = "La tabla de la base de datos se borro con exito"
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = "Borrar Registro"
        mensaje = "No hay tabla para borrar"
        messagebox.showerror(titulo,mensaje)


class Pelicula:
    def __init__(self, nombre, genero, calificacion):
        self.id_pelicula = None
        self.nombre = nombre
        self.genero = genero
        self.calificacion = calificacion
    def __str__(self):
        return f'Pelicula[{self.nombre},{self.genero},{self.calificacion}]'
    
def guardar(pelicula):
    conexion = ConexionDB()
    
    sql = f"""
    INSERT INTO peliculas (nombre,genero,calificacion) VALUES('{pelicula.nombre}' , '{pelicula.genero}' , '{pelicula.calificacion}')
    """
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Conexion al Registro"
        mensaje = "La tabla de peliculas no esta creada en la base de datos"
        messagebox.showerror(titulo,mensaje)

def listar():
    conexion = ConexionDB()
    lista_peliculas = []
    sql = "SELECT * FROM peliculas"
    try:
        conexion.cursor.execute(sql)
        lista_peliculas =  conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = "Conexion al Registro"
        mensaje = "Crea la tabla en la base de datos"
        messagebox.showwarning(titulo,mensaje)
    
    return lista_peliculas

def editar(pelicula, id_pelicula):
    conexion = ConexionDB()
    sql = f"""
    UPDATE peliculas
    set nombre  = '{pelicula.nombre}',
    genero="{pelicula.genero}",
    calificacion="{pelicula.calificacion}"
    WHERE id_pelicula={id_pelicula}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo="Edicion de datos"
        mensaje ="No se pudo editar el registro"
        messagebox.showerror(titulo,mensaje)

def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql = f"DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo="Eliminar Datos"
        mensaje ="No se pudo eliminar el registro"
        messagebox.showerror(titulo,mensaje)