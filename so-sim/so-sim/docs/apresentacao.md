# Apresentação — SO-Sim

## 1. Tema

Simulador de escalonamento de processos e gerenciamento de memória.

## 2. Problema abordado

Sistemas Operacionais precisam decidir:

- qual processo deve executar na CPU;
- por quanto tempo ele executa;
- como a memória será distribuída entre os processos.

O SO-Sim demonstra essas decisões por meio de algoritmos clássicos.

## 3. Objetivo do projeto

Criar uma ferramenta didática e reproduzível capaz de simular:

- escalonamento de CPU;
- gerenciamento de memória;
- comparação entre algoritmos;
- geração de métricas de desempenho.

## 4. Algoritmos de CPU implementados

### FCFS

Executa os processos na ordem de chegada.

### SJF

Escolhe o menor processo entre os que já chegaram.

### Round Robin

Executa processos por fatias de tempo chamadas quantum.

### Prioridade

Executa primeiro os processos com maior prioridade.

## 5. Algoritmos de memória implementados

### First Fit

Escolhe o primeiro bloco livre suficiente.

### Best Fit

Escolhe o menor bloco livre suficiente.

### Worst Fit

Escolhe o maior bloco livre disponível.

## 6. Métricas exibidas

### CPU

- tempo de espera;
- turnaround;
- médias;
- gráfico de Gantt.

### Memória

- memória total;
- memória utilizada;
- memória livre;
- taxa de ocupação;
- processos alocados e rejeitados.

## 7. Diferenciais do projeto

- Menu interativo.
- Cenário personalizado.
- Relatório completo CPU + memória.
- Gráfico de Gantt com linha do tempo.
- Código modular.
- Execução simples em qualquer máquina com Python.

## 8. Como demonstrar

Executar:

```bash
python main.py