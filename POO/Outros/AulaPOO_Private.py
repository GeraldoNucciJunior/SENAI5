class Exemplo_PO2:

    def __init__(self):
        self.__saldo_inicial = 0

    def get_saldo_inicial(self):
        return self.__saldo_inicial

    def set_saldo_inicial(self, saldo_inicial):
        self.__saldo_inicial = saldo_inicial



p = Exemplo_PO2()

print(p.get_saldo_inicial())
p.set_saldo_inicial(100)
print(p.get_saldo_inicial())


