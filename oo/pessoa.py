class Pessoa:

    def __init__(self, nome=None, idade=38):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return 'Criando Classe Objetos e Atributos'


if __name__ == "__main__":
    
    p = Pessoa('Wesley Pires')
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)