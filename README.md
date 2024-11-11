# M2_SO

## Análise de Page Faults em Sistemas Operacionais

Este projeto foi desenvolvido como parte da M2 na disciplina de Sistemas Operacionais no quinto período de Ciência da Computação, ministrada pelo professor Felipe Viel. O objetivo é aplicar e analisar o conceito de *page faults* em sistemas operacionais de propósito geral, como Windows e Linux, utilizando códigos em Python e C++ para realizar testes e observações de desempenho. O relatório e os códigos fornecem uma visão detalhada sobre o impacto de *minor faults* e *major faults* na paginação de memória.

### Conteúdo do Repositório

- **servidor.py**: Código do servidor em Python para monitoramento e simulação de demandas de memória.
- **cliente_num.py** e **cliente_str.py**: Clientes que enviam requisições de número e string, respectivamente, para o servidor.
- **memory_test.cpp**: Código em C++ para análise comparativa de desempenho em relação ao código em Python.
- **testememoria.py**: Código em Python para gerar alta demanda de memória e comparar resultados com o código equivalente em C++.
- **README.md**: Este documento explicativo, contendo detalhes do projeto, requisitos e estrutura de análise.

### Estrutura do Projeto e Requisitos

O projeto foca na análise de *page faults* em sistemas operacionais e inclui os seguintes requisitos:

1. **Identificação do autor e do trabalho**: Informações básicas sobre o autor e o propósito do projeto.
2. **Enunciado do Projeto**: Análise de *page faults* em sistemas operacionais, visando identificar e otimizar a alocação de memória.
3. **Explicação e Contexto**: Avaliação de *page faults* para identificar e analisar o desempenho de sistemas e aplicações, além de entender o comportamento de memória de cada sistema operacional.
4. **Resultados das Simulações**: Dados e observações obtidos durante os testes de desempenho, especialmente para *minor faults* e *major faults*.
5. **Códigos e Implementação**: Códigos relevantes para o projeto, tanto em Python quanto em C++.
6. **Análise de Resultados**: Tabelas e gráficos que comparam o desempenho de diferentes configurações de memória e threads.
7. **Comparação Multiplataforma**: Testes realizados tanto no Windows quanto no Linux, com diferentes configurações de carga.

### Descrição do Projeto

Este trabalho analisa o comportamento de *page faults* ao realizar simulações com diferentes alocações de memória e configurações de threads. O projeto permite observar como sistemas operacionais lidam com a alocação de memória sob carga pesada, fornecendo insights sobre o impacto de *minor faults* e *major faults* no desempenho.

### Ferramentas de Análise

Para obter métricas precisas sobre *page faults*, foram utilizadas as seguintes ferramentas:

- **Windows**: *Process Explorer* para monitoramento de memória e threads.
- **Linux**: Comandos `ps`, `top`, `htop` e outras ferramentas de análise para observar *page faults* sob diferentes cargas de memória.
- **Codespaces**: Ambientes de desenvolvimento remoto com pouca memória principal, permitindo a ocorrência frequente de *page faults*.

### Pontuação Extra

Para obter pontuação extra (até 1,0 ponto), foram implementados e comparados o mesmo algoritmo em duas linguagens diferentes: **Python** e **C++**. A comparação se concentra em observar o desempenho de cada linguagem sob alta demanda de memória, permitindo uma análise aprofundada de como cada linguagem e sistema operacional gerenciam a memória.

### Relatório

O relatório, incluído em PDF, contém:

1. Identificação do autor e descrição do trabalho.
2. Enunciado detalhado do projeto.
3. Explicação sobre o contexto e a aplicação do problema.
4. Resultados das simulações e observações, com tabelas e gráficos.
5. Discussão e análise dos resultados, evidenciando o impacto de diferentes configurações de memória e linguagem na ocorrência de *page faults*.

### Executando o Projeto

Para rodar os códigos e realizar testes:

1. Clone o repositório:
   ```bash
   git clone <URL do repositório>
   cd <nome-do-repositório>

2. Execute o servidor:
  ```bash
  python3 servidor.py
   ```

3. Execute os clientes:
```bash
python3 cliente_num.py
python3 cliente_str.py
```

4. Compile e execute o código em C++ para o teste de memória:
```bash
g++ -o memory_test memory_test.cpp -std=c++11 -pthread
./memory_test
```

5. Use códigos para analisar o desempenho
```bash
htop
top
watch -n 1 "ps -o min_flt,maj_flt -p <PID>
```



