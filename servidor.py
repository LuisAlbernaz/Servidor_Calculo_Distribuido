import socket
import threading

# Função que gerencia a conexão com cada cliente individualmente.
# Recebe a operação matemática enviada pelo cliente, exibe no servidor,
# e retorna o resultado após o processamento.
# Finaliza a conexão ao não receber mais dados.

def trata_cliente(conn, addr):
    print(f"Conectado com {addr}")
    while True:
        try:
            dados = conn.recv(1024).decode('utf-8')
            if not dados:
                break

            print(f"Recebido de {addr}: {dados}")

            try:
                resultado = eval(dados, {'__builtins__': None}, {})
            except Exception as e:
                resultado = f"Erro: {str(e)}"

            conn.send(str(resultado).encode('utf-8'))

        except Exception as e:
            print(f"Erro: {e}")
            break

    conn.close()
    print(f"Conexão com {addr} encerrada.")

HOST = 'localhost'  
PORTA = 12345       

# Cria o socket TCP/IP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))  # Associa o socket ao endereço e porta
servidor.listen()             


print("Servidor aguardando conexões...")

# Cada thread executa a função trata_cliente, que atende o cliente individualmente, permitindo múltiplos clientes conectados ao mesmo tempo.
while True:
    conn, addr = servidor.accept()
    cliente_thread = threading.Thread(target=trata_cliente, args=(conn, addr))
    cliente_thread.start()
