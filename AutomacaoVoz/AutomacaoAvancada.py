import speech_recognition as sr
import hashlib
import os


if not os.path.isfile('usuarios.txt'):
    open('usuarios.txt', 'a').close()



def criar_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()



def reconhecer_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo:")
        audio = r.listen(source)


    try:
        fala = r.recognize_google(audio, language='pt-BR')
        print("Você disse: " + fala)
        return fala
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o que você disse.")
    except sr.RequestError as e:
        print("Não foi possível se conectar ao serviço do Google; {0}".format(e))



def cadastrar_usuario():
    # Solicitar informações de identificação do usuário
    nome = input("Digite seu nome: ")
    print("Agora, por favor, diga sua senha para confirmar sua identidade.")

    # Loop para tentar reconhecer a senha do usuário
    senha = None
    while senha is None:
        senha = reconhecer_voz()


        if senha is None:
            print("Não foi possível reconhecer a senha. Por favor, tente novamente.")

    senha_hash = criar_hash(senha)

    with open('usuarios.txt', 'a') as f:
        f.write(nome + ',' + senha_hash + '\n')

    print("Usuário cadastrado com sucesso!")
    return nome, senha


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


usuarios = {}
with open('usuarios.txt', 'r') as f:
    for linha in f:
        partes = linha.strip().split(',')
        if len(partes) == 2:
            nome, senha_hash = partes
            usuarios[nome] = senha_hash

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

def solicitar_acao():
    pass


if verificar_identidade(nome_usuario):
    solicitar_acao()
