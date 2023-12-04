import sqlite3
class Consultas:
    def __init__(self) -> None:
        self.con = sqlite3.connect("mis_citas.db")
        self.cmd= self.con.cursor()
        self.table_citas = 'citas'
        self.table_clientes = 'gente'
        self.pers_cond = 'clave'

    def select(self, tabla):
        query = f'SELECT * FROM {tabla}'
        self.cmd.execute(query)
        rows = self.cmd.fetchall()
        return rows
    
    def registroExistente(self, tabla, condicion, llave):
        query = f'SELECT * FROM {tabla} where {condicion} = ?'
        self.cmd.execute(query,(llave,))
        row = self.cmd.fetchone()
        return row is not None
    
    def eliminarPers(self, tabla, condicion, value):
        query = f'DELETE FROM {tabla} WHERE {condicion} = ?'
        self.cmd.execute(query,(value,))


    def insertar_persona(self, data_list):
        query = "INSERT INTO gente (clave, nombre, email, celular, direccion) VALUES (?, ?, ?, ?, ?)"
        self.cmd.execute(query, data_list)
        self.con.commit()

    
    def insertCita(self):
        pass

