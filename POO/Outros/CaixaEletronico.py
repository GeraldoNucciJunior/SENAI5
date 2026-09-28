class CaixaEletronico:
    total = 0
    def depositar(self, a):
        self.total += a
    def sacar(self,a):
        self.total -= a
    def saldo(self):
        return self.total


caixa = CaixaEletronico()
caixa.depositar(10)
print(caixa.saldo())


caixa.sacar(3)
print(caixa.saldo())