import sqlite3

class DataBaseAdapter:
    #Conexión a la base de datos
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    #Permite ejecutar queries, solo ejecuta los query
    def excute_query(self, query, params=()):
        self.cursor.execute(query,params)
        self.conn.commit()

    #Hacer peticiones, capturar la respuesta anterior y retornarla
    def fetch_data(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    #Cerrar conexion
    def close_connection(self):
        self.conn.close()