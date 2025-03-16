import socket

HOST = '127.0.0.1'
PORTA = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, 12345))
    print("Conectado ao servidor. Digite 'sair' para encerrar.")

    while True:
        operacao = input("Digite a operação matemática (ex: 5+3): ")
        if operacao.lower() in ['sair', 'exit']:
            break

          
        cliente.sendall(operacao.encode('utf-8')) 
        resultado = cliente.recv(1024).decode('utf-8') 
        print(f"Resultado recebido: {resultado}")

cliente.close()

#sendall() envia dados em formato de bytes.
#recv() recebe dados pela rede em bytes.
#encode('utf-8') transforma texto em bytes.
#decode('utf-8') transforma bytes de volta em texto.
#AF_INET -> Determina que o endereço usado será do tipo IPv4.
#SOCK_STREAM -> Indica que a comunicação será do tipo TCP, orientada à conexão.