class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor


# Criar um objeto bola1
bola1 = Bola("vermelha", 10, "plástico")

# Mostrar a cor atual da bola1
print(bola1.mostraCor())  # Saída: vermelha

# Trocar a cor da bola1 para azul
bola1.trocaCor("azul")

# Mostrar a nova cor da bola1
print(bola1.mostraCor())  # Saída: azul


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa1 = Pessoa("João", 25)
