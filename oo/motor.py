class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade = self.velocidade + 1
        return self.velocidade

    def frear(self):
        if self.velocidade <= 1:
            self.velocidade = 0
        elif self.velocidade >= 0:
            self.velocidade = self.velocidade - 2
        return self.velocidade
        

if __name__ == "__main__":

    motor = Motor()
'''
    print(f'Carro parado na velocidade: {motor.velocidade}')
    motor.acelerar()
    print(f'Carro na velocidade: {motor.velocidade} km/h')
    motor.acelerar()
    print(f'Carro na velocidade: {motor.velocidade} km/h')
    motor.acelerar()
    print(f'Carro na velocidade: {motor.velocidade} km/h')
    motor.acelerar()
    print(f'Carro na velocidade: {motor.velocidade} km/h')
    motor.acelerar()
    motor.acelerar()
    print(f'Carro na velocidade: {motor.velocidade} km/h')
    motor.acelerar()
    print(f'Carro na velocidade: {motor.velocidade} km/h')
    motor.acelerar()
    print(f'Carro na velocidade: {motor.velocidade} km/h')
    motor.acelerar()
    print(f'Carro na velocidade: {motor.velocidade} km/h')
    motor.frear()
    print(f'Carro sendo freado e voltando a velocidade: {motor.velocidade} km/h')
    motor.frear()
    print(f'Carro sendo freado e voltando a velocidade: {motor.velocidade} km/h')
    motor.frear()
    print(f'Carro sendo freado e voltando a velocidade: {motor.velocidade} km/h')
    motor.frear()
    print(f'Carro sendo freado e voltando a velocidade: {motor.velocidade} km/h')
    motor.frear()
    print(f'Carro sendo freado e voltando a velocidade: {motor.velocidade} km/h')

'''