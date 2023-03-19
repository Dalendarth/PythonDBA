import speech_recognition as sr
import hashlib
import os

# Verificar se o arquivo de usuários existe
if not os.path.isfile('usuarios.txt'):
    # Se o arquivo não existe, criá-lo vazio
    open('usuarios.txt', 'a').close()


# Função para criar um hash seguro de uma string
def criar_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()


# Função para capturar e reconhecer a voz do usuário
def reconhecer_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo:")
        audio = r.listen(source)

    # Reconhecer a fala usando o serviço do Google
    try:
        fala = r.recognize_google(audio, language='pt-BR')
        print("Você disse: " + fala)
        return fala
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o que você disse.")
    except sr.RequestError as e:
        print("Não foi possível se conectar ao serviço do Google; {0}".format(e))


# Função para cadastrar um novo usuário
def cadastrar_usuario():
    # Solicitar informações de identificação do usuário
    nome = input("Digite seu nome: ")
    print("Agora, por favor, diga sua senha para confirmar sua identidade.")

    # Loop para tentar reconhecer a senha do usuário
    senha = None
    while senha is None:
        senha = reconhecer_voz()

        # Verificar se a senha foi reconhecida corretamente
        if senha is None:
            print("Não foi possível reconhecer a senha. Por favor, tente novamente.")

    senha_hash = criar_hash(senha)

    # Armazenar a voz do usuário e sua senha em um arquivo seguro
    with open('usuarios.txt', 'a') as f:
        f.write(nome + ',' + senha_hash + '\n')

    print("Usuário cadastrado com sucesso!")
    return nome, senha


# Função para verificar a identidade do usuário
def verificar_identidade(nome_usuario):
    senha_hash = usuarios[nome_usuario]
    tentativas = 3
    while tentativas > 0:
        print("Por favor, diga sua senha para confirmar sua identidade.")
        senha = reconhecer_voz()
        senha_hash_informada = criar_hash(senha)
        if senha_hash_informada == senha_hash:
            print("Identidade confirmada.")
            return True
        else:
            print("Senha incorreta. Você tem mais %d tentativas." % (tentativas - 1))
            tentativas -= 1

    print("Identidade não confirmada. Tente novamente mais tarde.")
    return False


# Carregar informações de usuários registrados de um arquivo seguro
usuarios = {}
with open('usuarios.txt', 'r') as f:
    for linha in f:
        partes = linha.strip().split(',')
        if len(partes) == 2:
            nome, senha_hash = partes
            usuarios[nome] = senha_hash

# Solicitar nome de usuário e verificar se ele está registrado
nome_usuario = input("Digite seu nome de usuário: ")
if nome_usuario not in usuarios:
    print("Usuário não registrado.")
    print("Deseja cadastrar um novo usuário? (s/n)")
    resposta = input().strip().lower()
    if resposta == 's':
        nome_usuario, senha_usuario = cadastrar_usuario()
        usuarios[nome_usuario] = senha_usuario
    else:
        exit()

# Verificar a identidade do usuário
def solicitar_acao():

if verificar_identidade(nome_usuario):
    solicitar_acao()
