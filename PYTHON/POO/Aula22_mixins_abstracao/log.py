# Abstração  -> É utlizada quando não se quer quer a classe seja utilizada diretamente.

class Log:
    def log(self, msg):  # assinatura do método
        raise NotImplementedError('Implemente o método log')
    


class LogFileMixin(Log):
    def log(self, msg):
        print(msg)








if __name__ == '__main__':
    l = Log()
    l.log('qualquer coisa')