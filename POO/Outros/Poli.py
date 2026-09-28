class Forma:
    def calcular_area(self):
     return 0

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado**2


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def calcular_area(self):
        return self.largura * self.altura

def exibir_area     (forma:Forma):
    print(forma.calcular_area())



exibir_area(Retangulo(10,10))


