# cd(caminho)
# python3 / python testememoria.py
#  pgrep -f testememoria.py
# watch -n 1 "ps -o min_flt,maj_flt -p <PID>

import numpy as np
import time
import threading

# Define o tamanho da matriz
MATRIX_SIZE = 1000  # Pode ajustar para aumentar ou diminuir a carga
NUM_THREADS = 4  # Número de threads para paralelizar o processamento

def process_matrix():
    # Gera duas matrizes grandes aleatórias e multiplica
    matrix_a = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
    matrix_b = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
    
    # Realiza a multiplicação de matrizes
    result = np.dot(matrix_a, matrix_b)
    
    # Simula algum tempo de processamento adicional
    time.sleep(1)
    
    # Retorna o resultado apenas para manter referência (não é essencial para a análise)
    return result

def start_processing():
    threads = []
    
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=process_matrix)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    while True:
        print("Iniciando processamento de matriz...")
        start_processing()
        print("Processamento concluído. Repetindo...")
        time.sleep(2)  # Intervalo entre processamentos
