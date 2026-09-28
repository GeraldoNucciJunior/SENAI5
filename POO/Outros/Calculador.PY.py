class Calculo:
    numero01=0
    numero02=0

    def soma1(self   ):
        self.numero01=float(input("Digite um numero: "))
        self.numero02=float(input("Digite outro numero: "))
        total=self.numero01+self.numero02
        print("total do calculo: ",total)

    def soma2(self, a, b):
        self.numero01 = a
        self.numero02 = b
        total = self.numero01 + self.numero02
        print("total do calculo: ", total)





calculadora = Calculo()
calculadora.soma1()
calculadora.soma2(1,2)