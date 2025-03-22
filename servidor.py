import socket
import threading
import datetime

def trata_cliente(conn, addr):
    print(f"Conectado com {addr}")
    while True:
        try:
            dados = conn.recv(1024).decode('utf-8').strip()
            if not dados:
                break

            print(f"Recebido de {addr}: {dados}")

            resultado = calcular(dados)
            
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            resposta = f"Resultado: {resultado} | Data/Hora: {timestamp}"

            conn.send(str(resposta).encode('utf-8'))

        except Exception as e:
            print(f"Erro: {e}")
            break

    conn.close()
    print(f"Conexão com {addr} encerrada.")

def calcular(expressao):
    """ Processa expressões matemáticas simples de forma segura. """
    try:
        expressao = expressao.replace(" ", "")
        
        permitido = "0123456789+-*/()."
        if any(char not in permitido for char in expressao):
            return "Erro: Expressão inválida"

        return eval(expressao, {"__builtins__": None}, {})
    except Exception:
        return "Erro: Cálculo inválido"
    
def iniciar_servidor(host='localhost', porta=12345):
    """ Inicia o servidor e escuta conexões. """
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()
    
    print(f"Servidor rodando em {host}:{porta}...")

    try:
        while True:
            conn, addr = servidor.accept()
            cliente_thread = threading.Thread(target=trata_cliente, args=(conn, addr))
            cliente_thread.start()
    except KeyboardInterrupt:
        print("Encerrando servidor...")
    finally:
        servidor.close()

if __name__ == "__main__":
    iniciar_servidor()