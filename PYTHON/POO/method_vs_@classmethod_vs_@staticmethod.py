# method vs @classmethod vs @staticmethod

# method - self, método de instância

# @classmethod - cls, método de classe | Recebe a classe

# @staticmethod - método estático (❌self, ❌cls)


class Connection:
    def __ini__(self, host='local@host'):
        # ↓ Método de instãncia
        self.host = host
        self.user = None
        self.password = None

    # setter
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password =password



    @classmethod  # Método de classe
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection



    @staticmethod
    def soma(a, b):
        return a + b


c1 = Connection()
""" c1.set_user('Luiz')
c1.set_password('123') """
print(c1.user)