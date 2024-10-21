class MySQLAdapter:
    def __init__(self, db_name):
        import mysql.connector # type: ignore
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database=db_name
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_data(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()
