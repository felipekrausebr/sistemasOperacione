# SO-Sim — Simulador de Sistemas Operacionais

## Descrição

O SO-Sim é um simulador didático de Sistemas Operacionais desenvolvido em Python. O projeto demonstra, de forma prática, conceitos de escalonamento de processos e gerenciamento de memória.

O simulador permite executar algoritmos clássicos de CPU, estratégias de alocação de memória, comparação de desempenho e geração de relatório completo do sistema.

## Funcionalidades

* Escalonamento FCFS.
* Escalonamento SJF não preemptivo.
* Escalonamento Round Robin com quantum.
* Escalonamento por Prioridade.
* Gerenciamento de memória com First Fit.
* Gerenciamento de memória com Best Fit.
* Gerenciamento de memória com Worst Fit.
* Gráfico de Gantt com linha do tempo.
* Comparação entre algoritmos de escalonamento.
* Criação de cenário personalizado.
* Relatório completo integrando CPU e memória.

## Tecnologias utilizadas

* Python 3
* VS Code
* Windows 11

## Estrutura do projeto

```text
so-sim/
├── main.py
├── README.md
├── docs/
│   └── apresentacao.md
├── examples/
└── src/
    ├── process.py
    ├── scheduler.py
    ├── memory.py
    └── utils.py
```

## Como executar

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

## Menu principal

```text
1 - FCFS
2 - SJF
3 - Round Robin
4 - Prioridade
5 - Memória: First Fit
6 - Memória: Best Fit
7 - Memória: Worst Fit
8 - Comparar Algoritmos
9 - Cenário Personalizado
10 - Relatório Completo CPU + Memória
0 - Sair
```

## Algoritmos de escalonamento

### FCFS

Executa os processos na ordem de chegada. É um algoritmo simples, não preemptivo.

### SJF

Seleciona o processo com menor tempo de CPU entre os processos já disponíveis na fila de prontos.

### Round Robin

Executa os processos em fatias de tempo chamadas quantum. Caso o processo não termine dentro do quantum, ele volta para a fila.

### Prioridade

Seleciona o processo com maior prioridade entre os processos disponíveis. Neste projeto, menor número significa maior prioridade.

## Algoritmos de memória

### First Fit

Aloca o processo no primeiro bloco livre com espaço suficiente.

### Best Fit

Aloca o processo no menor bloco livre que ainda comporta o processo.

### Worst Fit

Aloca o processo no maior bloco livre disponível.

## Métricas calculadas

### CPU

* Tempo de início.
* Tempo de finalização.
* Tempo de espera.
* Turnaround time.
* Média de espera.
* Média de turnaround.

### Memória

* Memória total.
* Memória utilizada.
* Memória livre.
* Taxa de ocupação.
* Processos alocados.
* Processos rejeitados.

## Objetivo acadêmico

O objetivo do projeto é demonstrar como diferentes algoritmos de Sistemas Operacionais impactam a execução de processos e o uso da memória.

A proposta é servir como ferramenta didática para visualizar decisões típicas de um sistema operacional, como escolha do próximo processo a executar e alocação de memória para processos.
