// cd(caminho)
// g++ memoriateste.cpp -o memory_teste -std=c++11 -pthread
// ./memory_teste
// ps aux | grep memory_teste
// watch -n 1 "ps -o min_flt,maj_flt -p <PID>

#include <iostream>
#include <vector>
#include <thread>
#include <random>
#include <chrono>

const int MATRIX_SIZE = 1000; // Tamanho da matriz (pode ajustar para gerar mais carga)
const int NUM_THREADS = 4;    // Número de threads

// Função para gerar uma matriz de números aleatórios
std::vector<std::vector<double>> generate_matrix(int size) {
    std::vector<std::vector<double>> matrix(size, std::vector<double>(size));
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);

    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            matrix[i][j] = dis(gen);
        }
    }
    return matrix;
}

// Função para multiplicar duas matrizes
void multiply_matrices(const std::vector<std::vector<double>>& matrix_a,
                       const std::vector<std::vector<double>>& matrix_b,
                       std::vector<std::vector<double>>& result,
                       int start_row, int end_row) {
    int size = matrix_a.size();
    for (int i = start_row; i < end_row; ++i) {
        for (int j = 0; j < size; ++j) {
            result[i][j] = 0;
            for (int k = 0; k < size; ++k) {
                result[i][j] += matrix_a[i][k] * matrix_b[k][j];
            }
        }
    }
}

void process_matrix() {
    auto matrix_a = generate_matrix(MATRIX_SIZE);
    auto matrix_b = generate_matrix(MATRIX_SIZE);
    std::vector<std::vector<double>> result(MATRIX_SIZE, std::vector<double>(MATRIX_SIZE, 0));

    // Divide o trabalho entre threads
    std::vector<std::thread> threads;
    int rows_per_thread = MATRIX_SIZE / NUM_THREADS;

    for (int i = 0; i < NUM_THREADS; ++i) {
        int start_row = i * rows_per_thread;
        int end_row = (i == NUM_THREADS - 1) ? MATRIX_SIZE : start_row + rows_per_thread;
        threads.push_back(std::thread(multiply_matrices, std::ref(matrix_a), std::ref(matrix_b), std::ref(result), start_row, end_row));
    }

    // Espera todas as threads terminarem
    for (auto& t : threads) {
        t.join();
    }
}

int main() {
    while (true) {
        std::cout << "Iniciando processamento de matriz..." << std::endl;
        process_matrix();
        std::cout << "Processamento concluído. Repetindo..." << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(2)); // Intervalo entre os processamentos
    }

    return 0;
}
