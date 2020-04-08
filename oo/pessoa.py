class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=38):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Criando Classe Objetos e Atributos'


    @staticmethod
    def metodo_estatico():
        return 42 + 3

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    print(Pessoa.metodo_estatico(), wesley.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), wesley.nome_e_atributo_de_classe())