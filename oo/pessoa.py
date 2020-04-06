class Pessoa:

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