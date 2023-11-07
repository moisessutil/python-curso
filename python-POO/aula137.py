class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabreicante(self, valor):
        self._fabricante = valor

    def mostrar(self):
        print(f'Carro: {self.nome}')
        print(f'Motor: {self._motor.nome}')
        print(f'Fabricante: {self._fabricante.nome}')
    

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

gol = Carro('Gol')
ea111 = Motor('EA111')
gol.motor = ea111
volks = Fabricante('Volkswagen')
gol.fabreicante = volks

gol.mostrar()


