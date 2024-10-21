class User:
    def __init__(self, name):
        self.name = name

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)

class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)

#Método que permite guardar datos
class UserFactory:
    @staticmethod
    def create_user(user_type, name):
        if user_type == "administrador":
            return AdminUser(name)
        elif user_type == "regular":
            return RegularUser(name)
        else:
            raise ValueError("Tipo de usuario no permitido")