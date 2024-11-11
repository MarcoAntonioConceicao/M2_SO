import os
import time

STR_REQ_PIPE = '/tmp/str_req_pipe'
STR_RESP_PIPE = '/tmp/str_resp_pipe'

def request_string():
    # Enviar solicitação de string
    with open(STR_REQ_PIPE, 'w') as str_pipe:
        str_pipe.write("Request string\n")
    
    time.sleep(0.5) 
    with open(STR_RESP_PIPE, 'r') as str_pipe:
        response = str_pipe.read().strip()
        print(f"Cliente: Resposta recebida -> {response}")

if __name__ == "__main__":
    while True:
        request_string()
        time.sleep(3)  # Intervalo entre requisições
