class Pessoa:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):
    def __init__(self,nome,cpf,limite_credito   ):
        super().__init__(nome,cpf)
        self.limite_credito = limite_credito




c = Cliente("Maria","171", 1234.12)
print (c.limite_credito)