class funcionario:
    def __init__(self, salario  ):
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario



d = funcionario(100)
print(d.salario)


d.salario = 200
print(d.salario)