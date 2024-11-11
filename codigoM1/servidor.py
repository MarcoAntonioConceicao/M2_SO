# cd(caminho)
# python3 servidor.py
# pgrep -f servidor.py
# watch -n 1 "ps -o min_flt,maj_flt -p <PID>

import os
import threading
import time
import random
from queue import Queue

# Pipes para números e strings
NUM_REQ_PIPE = '/tmp/num_req_pipe'
NUM_RESP_PIPE = '/tmp/num_resp_pipe'
STR_REQ_PIPE = '/tmp/str_req_pipe'
STR_RESP_PIPE = '/tmp/str_resp_pipe'

# Verifique e crie os pipes, se necessário
if not os.path.exists(NUM_REQ_PIPE):
    os.mkfifo(NUM_REQ_PIPE)

if not os.path.exists(NUM_RESP_PIPE):
    os.mkfifo(NUM_RESP_PIPE)

if not os.path.exists(STR_REQ_PIPE):
    os.mkfifo(STR_REQ_PIPE)

if not os.path.exists(STR_RESP_PIPE):
    os.mkfifo(STR_RESP_PIPE)

# Filas para armazenar respostas
num_response_queue = Queue()
str_response_queue = Queue()


# Locks para sincronização de acesso aos pipes
num_lock = threading.Lock()
str_lock = threading.Lock()

# Função para responder requisições de números
def handle_number_requests():
    while True:
        with num_lock:
            with open(NUM_REQ_PIPE, 'r') as num_pipe:
                request = num_pipe.read().strip()
                if request:
                    print(f"Servidor: Recebida solicitação de número: {request}")
                    response = f"Número gerado: {random.randint(1, 100)}\n"
                    num_response_queue.put(response)  # Adiciona a resposta na fila
                    print("Servidor: Resposta de número enfileirada.")
                    time.sleep(0.5)

# Função para responder requisições de strings
def handle_string_requests():
    while True:
        with str_lock:
            with open(STR_REQ_PIPE, 'r') as str_pipe:
                request = str_pipe.read().strip()
                if request:
                    print(f"Servidor: Recebida solicitação de string: {request}")
                    response = f"String resposta: 'Olá Cliente!'\n"
                    str_response_queue.put(response)  # Adiciona a resposta na fila
                    print("Servidor: Resposta de string enfileirada.")
                    time.sleep(0.5)

# Thread dedicada para enviar respostas de números
def send_number_responses():
    while True:
        response = num_response_queue.get()  # Pega a resposta da fila
        with open(NUM_RESP_PIPE, 'w') as num_pipe_w:
            num_pipe_w.write(response)
        print("Servidor: Resposta de número enviada.")
        time.sleep(0.5)  # Pausa para garantir a entrega

# Thread dedicada para enviar respostas de strings
def send_string_responses():
    while True:
        response = str_response_queue.get()  # Pega a resposta da fila
        with open(STR_RESP_PIPE, 'w') as str_pipe_w:
            str_pipe_w.write(response)
        print("Servidor: Resposta de string enviada.")
        time.sleep(0.5)  # Pausa para garantir a entrega

# Função principal do servidor que cria o pool de threads
def start_server(num_threads_number=5, num_threads_string=5):
    print("Servidor iniciado...")

    # Criar pool de threads
    threads = []

    # Criar múltiplas threads para requisições de números
    for _ in range(num_threads_number):
        t_number = threading.Thread(target=handle_number_requests)
        threads.append(t_number)

    # Criar múltiplas threads para requisições de strings
    for _ in range(num_threads_string):
        t_string = threading.Thread(target=handle_string_requests)
        threads.append(t_string)

    # Thread dedicada para enviar respostas
    threads.append(threading.Thread(target=send_number_responses))
    threads.append(threading.Thread(target=send_string_responses))

    # Iniciar todas as threads
    for t in threads:
        t.start()

    # Manter o servidor rodando
    for t in threads:
        t.join()

if __name__ == "__main__":
    start_server(num_threads_number=10, num_threads_string=10)
