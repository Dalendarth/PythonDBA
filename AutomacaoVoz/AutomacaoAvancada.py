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
    senha = reconhecer_voz()
    senha_hash = criar_hash(senha)

    # Armazenar a voz do usuário e sua senha em um arquivo seguro
    with open('usuarios.txt', 'a') as f:
        f.write(nome + ',' + senha_hash + '\n')

    print("Usuário cadastrado com sucesso!")
    return nome, senha


# Função para verificar a identidade do usuário
def verificar_identidade(senha_hash):
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


# Função para solicitar a senha do usuário para executar uma ação
def solicitar_acao(senha_destravar=10, senha_travar=10):
    print("Por favor, diga 'travar' ou 'destravar' para realizar a ação desejada.")
    acao = reconhecer_voz()
    if acao == senha_travar:
        print("Travando o desktop...")
        # Código para travar o desktop
    elif acao == senha_destravar:
        print("Destravando o desktop...")
        # Código para destravar o desktop
    else:
        print("Ação inválida. Tente novamente.")
        solicitar_acao()


# Carregar informações de usuários registrados de um arquivo seguro
usuarios = {}
with open('usuarios.txt', 'r') as f:
    for linha in f:
        partes = linha.strip().split(',')
        if len(partes) == 2:
            nome, senha_hash = partes
            usuarios[nome] = senha_hash
        else:
            print("Erro na linha do arquivo 'usuarios.txt':", linha)

# Solicitar o nome do usuário
nome_usuario = input("Por favor, diga seu nome: ")
if nome_usuario in usuarios:
    senha_hash = usuarios[nome_usuario]
else:
    print("Usuário não encontrado. Tente novamente.")
