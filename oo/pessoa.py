class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=38):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Criando Classe Objetos e Atributos'


if __name__ == "__main__":
    
    wesley = Pessoa(nome='Wesley')
    pires  = Pessoa(wesley, nome='Pires')
    print(pires.cumprimentar())
    print(pires.nome)
    print(pires.idade)
    for filho in pires.filhos:
        print(filho.nome)
    pires.sobrenome = 'Rosa'
    print(pires.sobrenome)
    del pires.filhos
    print(pires.__dict__)
    print(wesley.__dict__)
    print(Pessoa.olhos)
    print(wesley.olhos)
    print(pires.olhos)