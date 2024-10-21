import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from busines_logic.user_service import UserService
from data_access.database import DataBaseAdapter
from desing_patterns.adapter import MySQLAdapter

if __name__ == "__main__":
    use_mysql = False  # True para usar MySQL

    if use_mysql:
        db_adapter = MySQLAdapter("myapp_database")
    else:
        db_adapter = DataBaseAdapter("users.db")

    db_adapter.excute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, type TEXT, NAME text)")

    user_service = UserService(db_adapter)

    # Crear algunos usuarios
    user_service.create_user("administrador", "Mateo Hincapie")
    user_service.create_user("regular", "Andrea Muñoz")

    # Mostrar usuarios creados
    users = user_service.get_users()
    print("Listado de usuarios")
    for user in users:
        print(user)

    db_adapter.close_connection()
