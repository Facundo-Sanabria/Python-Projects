#Este es el módulo donde cargo todas las funcionalidades internas del programa

import sqlite3
from tkinter import scrolledtext as st

class ConnectionDB:

    def abrir(self):
        conexion = sqlite3.connect("bd1.db",detect_types=sqlite3.PARSE_DECLTYPES |
                                           sqlite3.PARSE_COLNAMES)
        try:
            conexion.execute("""create table libros (
                              Id integer primary key AUTOINCREMENT,
                              Título text,
                              Autor text,
                              Edición integer,
                              Impresión text,
                              Editorial text,
                              Traducción text,
                              Páginas integer,
                              Condición text
                            )""")                     
        except sqlite3.OperationalError:
            print("La tabla libros ya existe")
        return conexion
    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "insert into libros(Título,Autor,Edición,Impresión,Editorial,Traducción,Páginas,Condición) values (?,?,?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    def modifica(self,x):
        cone = self.abrir()
        cursor = cone.cursor()
        cursor.execute("UPDATE libros SET Autor=?, Edición=?, Impresión=?, Editorial=?, Traducción=?, Páginas=?, Condición=? WHERE Título=?",x)
        cone.commit()
        cone.close()
    def modificaestado(self,x):
        cone = self.abrir()
        cursor = cone.cursor()
        cursor.execute("UPDATE libros SET Condición=? WHERE Título=?",x)
        cone.commit()
        cone.close()
    def consulta(self, datos):
        cone = self.abrir()
        try:
            cursor = cone.cursor()
            sql = "select Autor, Edición, Impresión, Editorial, Traducción, Páginas, Condición from libros where Título=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
    def consultacondicion(self, datos):
        cone = self.abrir()
        try:
            cursor = cone.cursor()
            sql = "select Condición from libros where Título=?"
            cursor.execute(sql, datos)
            return cursor.fetchone()
        finally:
            cone.close()
    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select Título, Autor, Edición, Impresión, Editorial, Traducción, Páginas, Condición from libros"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
    def borrar(self,x):
        cone = self.abrir()
        cursor = cone.cursor()
        cursor.execute("delete from libros where Título=?", x)
        cone.commit()
        cone.close()
    
    def abrirprestamo(self):
        conexion = sqlite3.connect("bd1.db",detect_types=sqlite3.PARSE_DECLTYPES |
                                           sqlite3.PARSE_COLNAMES)
        try:
            conexion.execute("""create table prestamos (
                              Id integer primary key AUTOINCREMENT,
                              Nombre text,
                              Apellido text,
                              Teléfono integer,
                              Mail text,
                              FechaI timestamp,
                              Días integer,
                              Título text
                            )""")                     
        except sqlite3.OperationalError:
            print("La tabla prestamos ya existe")
        return conexion
    def altaprestamo(self, datos):
        cone = self.abrirprestamo()
        cursor = cone.cursor()
        sql = "insert into prestamos(Título,Nombre,Apellido,Teléfono,Mail,FechaI,Días) values (?,?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    def consultaprestamo(self, datos):
        cone = self.abrirprestamo()
        try:
            cursor = cone.cursor()
            sql = "select Nombre, Apellido, Teléfono, Mail, FechaI, Días from prestamos where Título=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
    def recuperar_todos_prestamo(self):
        try:
            cone=self.abrirprestamo()
            cursor=cone.cursor()
            sql="select Título, Nombre, Apellido, Teléfono, Mail, FechaI, Días from prestamos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
    def borrarprestamo(self,x):
        cone = self.abrirprestamo()
        cursor = cone.cursor()
        cursor.execute("delete from prestamos where Título=?", x)
        cone.commit()
        cone.close()