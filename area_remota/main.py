import socket
import re
import tkinter as tk

# Definindo inf de conexão
HOST = 'localhost'  # endereço server
PORT = 5000  # porta de uso server

HOST = socket.getaddrinfo(HOST, None, socket.AF_INET, socket.SOCK_STREAM)[0][4][0]

# objeto socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
sock.connect((HOST, PORT))

# boas vindas ao servidor
mensagem = sock.recv(1024)
print(mensagem.decode())


# Restante do código...

# Função para validar a senha
def validar_senha(senha):
    if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", senha):
        print("A senha deve ter no mínimo 8 caracteres e números")
        return False
    return True


# Função para enviar as informações de usuário e senha para o servidor
def enviar_info():
    # Obtendo os dados de usuário e senha da interface
    nome = nome_entry.get()
    senha = senha_entry.get()

    # Validando a senha
    if not validar_senha(senha):
        return

    # Enviando as informações de usuário e senha para o servidor
    dados = f'{nome}:{senha}'.encode()
    sock.sendall(dados)

    # Recebendo a resposta do servidor
    resposta = sock.recv(1024)
    resposta_decodificada = resposta.decode()

    # Verificando a resposta do servidor
    if resposta_decodificada == "OK":
        resposta_label.configure(text="Usuário validado com sucesso!")
    else:
        resposta_label.configure(text="Usuário ou senha inválidos.")


# Criando a janela da interface
janela = tk.Tk()
janela.title("Validação de Usuário")
janela.deiconify()

# Criando as caixas de entrada de dados
nome_label = tk.Label(janela, text="Nome de Usuário:")
nome_label.pack()
nome_entry = tk.Entry(janela)
nome_entry.pack()

senha_label = tk.Label(janela, text="Senha:")
senha_label.pack()
senha_entry = tk.Entry(janela, show="*")
senha_entry.pack()

# Criando o botão para enviar os dados
enviar_button = tk.Button(janela, text="Enviar", command=enviar_info)
enviar_button.pack()

# Criando a label para mostrar a resposta do servidor
resposta_label = tk.Label(janela, text="")
resposta_label.pack()

# Iniciando a janela
janela.mainloop()

# Fechando a conexão
sock.close()
