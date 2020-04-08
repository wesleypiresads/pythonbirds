from motor import Motor
from direcao import Direcao

class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor
    
    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()
    
    def frear(self):
        self.motor.frear()
    
    def calcular_direcao(self):
        return self.direcao.direcao
    
    def direita(self):
        self.direcao.virar_a_direita()
    
    def esquerda(self):
        self.direcao.virar_a_esquerda()

if __name__ == "__main__":

    motor = Motor()
    direcao = Direcao()
    carro = Carro(direcao, motor)
    
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.frear()
    print(carro.calcular_velocidade())
    carro.frear()
    print(carro.calcular_velocidade())

    print(carro.calcular_direcao())
    carro.direita()
    print(carro.calcular_direcao())
    carro.direita()
    print(carro.calcular_direcao())
    carro.direita()
    print(carro.calcular_direcao())
    carro.esquerda()
    print(carro.calcular_direcao())
    carro.esquerda()
    print(carro.calcular_direcao())