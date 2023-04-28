import socket

# Define as informações de conexão do servidor
HOST = 'localhost'  # endereço local
PORT = 5000  # porta para uso do servidor

# Cria um objeto socket para o servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao endereço e porta especificados
sock.bind((HOST, PORT))

# Inicia o servidor e espera por conexões de clientes
sock.listen()

while True:
    # Espera por uma conexão
    conn, addr = sock.accept()

    # Exibe informações sobre a conexão
    print(f"Conexão estabelecida com {addr}")

    # Recebe dados enviados pelo cliente
    dados = conn.recv(1024)

    # Exibe os dados recebidos
    print(f"Dados recebidos: {dados.decode()}")

    # Envia uma resposta para o cliente
    resposta = "Recebido!"
    conn.sendall(resposta.encode())

    # Fecha a conexão com o cliente
    conn.close()
