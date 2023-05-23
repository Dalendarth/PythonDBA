class human:
    def __init__(self, idade, caracteristica, status):
        self.idade = idade
        self.caracteristica = caracteristica
        self.status = status


# Criar um objeto 'pessoa' da classe 'human'
pessoa = human(30, "Morena", "Solteira")

# Acessar os atributos do objeto
print(pessoa.idade)  # Saída: 30
print(pessoa.caracteristica)  # Saída: Morena
print(pessoa.status)  # Saída: Solteira
