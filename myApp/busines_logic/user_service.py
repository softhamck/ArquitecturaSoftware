from desing_patterns.factory import UserFactory
from desing_patterns.observer import UserObserver
from data_access.database import DataBaseAdapter

class UserService: 
    def __init__(self, db_adapter):
        self.db_adapter = db_adapter
        self.observe = UserObserver()

    def create_user(self, user_type, name):
        user = UserFactory.create_user(user_type, name)
        self.db_adapter.excute_query(
            "INSERT INTO users (type, name) values(?,?)", (user_type, name)
        )
        self.observe.notify(f"El usuario {name}, de tipo {user_type}, se ha creado con éxito...")
        return user

    def get_users(self):
        users = self.db_adapter.fetch_data("SELECT * FROM users")
        return users
    
    