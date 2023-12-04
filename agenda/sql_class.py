import sqlite3
import os
class Consultas:
    def __init__(self) -> None:
        self.con = sqlite3.connect("mis_citas.db")
        self.cmd= self.con.cursor()
        self.table_clientes = 'gente'
        self.pers_cond = 'clave'
        self.pers_cols = ["clave", "nombre", "celular", "email", "direccion"]
        self.table_citas = 'citas'

    def crear_bd(self):
        nombre_bd = 'mis_citas.db'

        if os.path.isfile(nombre_bd):
            print(f"El archivo {nombre_bd} existe.")
        else:
            print(f"El archivo {nombre_bd} no existe o no es un archivo regular.")

    def select(self, tabla):
        query = f'SELECT * FROM {tabla}'
        self.cmd.execute(query)
        rows = self.cmd.fetchall()
        return rows
    
    def insertar(self, n_tabla, columnas, data_list):
        columns = ', '.join(columnas)
        placeholders = ', '.join(['?' for _ in columnas])
        query = f"INSERT INTO {n_tabla} ({columns}) VALUES ({placeholders})"
        self.cmd.execute(query, data_list)
        self.con.commit()
    
    def update(self, n_tabla, columnas, data_list, condicion, value):
        set_query = ', '.join([f"{col} = ?" for col in columnas])
        query = f"UPDATE {n_tabla} SET {set_query} WHERE {condicion} = ?"
        data_list.append(value)
        self.cmd.execute(query, data_list)
        self.con.commit()

    def eliminar(self, tabla, condicion, value):
        query = f'DELETE FROM {tabla} WHERE {condicion} = ?'
        self.cmd.execute(query,(value,))
        self.con.commit()

    def registroExistente(self, tabla, condicion, llave):
        query = f'SELECT * FROM {tabla} where {condicion} = ?'
        self.cmd.execute(query,(llave,))
        row = self.cmd.fetchone()
        return row is not None
    
    def insertCita(self):
        pass

