""" 
    method vs @classmethod

    method - self, método de instância

    @classmethod - cls, método da classe

    Sempre que é preciso usar o "self", isso é um método de instância
"""

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None


    # configurando o user
    def set_user(self, user):
        self.user = user

    # configurando o password
    def set_password(self, password):
        self.password = password


    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection




c1 = Connection()
c1.set_user('José')
c1.set_password('123')

print(c1.user)
print(c1.password)

con = Connection.create_with_auth('jouber', '456')
print(con.user)
print(con.password)
