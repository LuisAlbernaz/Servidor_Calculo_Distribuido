import socket
import threading
import random

OPERACOES = [
    "10 + 5",
    "20 - 3",
    "7 * 8",
    "50 / 2",
    "2 + 3 * 4",
    "(10 + 2) * 5",
    "100 / (4 + 1)",
    "3.5 * 2",
]

HOST = 'localhost'
PORTA = 12345
NUM_CONEXOES = 5

def cliente_thread(id):
    """ Função que representa um cliente enviando uma operação matemática """
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((HOST, PORTA))
        
        expressao = random.choice(OPERACOES)
        print(f"[Cliente {id}] Enviando: {expressao}")

        cliente.sendall(expressao.encode('utf-8'))

        resultado = cliente.recv(1024).decode('utf-8')
        print(f"[Cliente {id}] Resultado: {resultado}")

        cliente.close()

    except Exception as e:
        print(f"[Cliente {id}] Erro: {e}")

threads = []
for i in range(NUM_CONEXOES):
    t = threading.Thread(target=cliente_thread, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Todos os clientes finalizaram as operações.")
