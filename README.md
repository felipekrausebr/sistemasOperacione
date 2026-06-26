# SO-Sim

Simulador de Sistemas Operacionais desenvolvido em Python.


## Funcionalidades

### Escalonamento de CPU

* FCFS (First Come First Served)
* SJF (Shortest Job First)
* Escalonamento por Prioridade

### Gerenciamento de Memória

* First Fit
* Best Fit
* Worst Fit

### Interface Gráfica

Desenvolvida com Streamlit.

Permite:

* Criar processos personalizados
* Executar algoritmos de escalonamento
* Simular gerenciamento de memória
* Visualizar gráfico de Gantt-
* Visualizar estatísticas do sistema
* Dashboard com indicadores

## Instalação

Instale as dependências:

```bash
pip install -r requirements.txt ou python -m pip install -r requirements.txt
```

## Execução

### Interface Web

```bash
python -m streamlit run app.py
```

### Versão Terminal

```bash
python main.py
```

## Estrutura do Projeto

```text
src/
├── process.py
├── scheduler.py
├── memory.py
└── utils.py
```

## Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* Matplotlib

## Cenários de Teste

A seguir são apresentados alguns cenários para validação dos algoritmos implementados no simulador.

---

## Cenário 1 — FCFS (First Come, First Served)

**Objetivo:** validar a execução dos processos por ordem de chegada.

### Processos

| Processo | Chegada | CPU | Prioridade | Memória (MB) |
|----------|---------|-----|------------|--------------|
| P1 | 0 | 6 | 3 | 120 |
| P2 | 1 | 4 | 1 | 80 |
| P3 | 2 | 8 | 4 | 200 |
| P4 | 3 | 3 | 2 | 100 |
| P5 | 4 | 5 | 5 | 150 |

### Ordem esperada

```
P1 → P2 → P3 → P4 → P5
```

---

## Cenário 2 — SJF (Shortest Job First)

**Objetivo:** validar a ordenação dos processos pelo menor tempo de CPU.

### Processos

| Processo | Chegada | CPU | Prioridade | Memória (MB) |
|----------|---------|-----|------------|--------------|
| P1 | 0 | 7 | 3 | 120 |
| P2 | 1 | 2 | 1 | 80 |
| P3 | 2 | 5 | 4 | 100 |
| P4 | 3 | 1 | 2 | 60 |
| P5 | 4 | 4 | 5 | 150 |

### Ordem esperada

```
P4 → P2 → P5 → P3 → P1
```

---

## Cenário 3 — Prioridade

**Objetivo:** validar a ordenação dos processos por prioridade.

> Menor número = maior prioridade.

### Processos

| Processo | Chegada | CPU | Prioridade | Memória (MB) |
|----------|---------|-----|------------|--------------|
| P1 | 0 | 6 | 4 | 120 |
| P2 | 1 | 3 | 1 | 80 |
| P3 | 2 | 5 | 3 | 200 |
| P4 | 3 | 2 | 2 | 100 |
| P5 | 4 | 4 | 5 | 150 |

### Ordem esperada

```
P2 → P4 → P3 → P1 → P5
```

---

## Cenário 4 — First Fit

**Objetivo:** validar a alocação utilizando o algoritmo First Fit.

### Blocos de memória

| Bloco | Tamanho |
|-------|----------|
| B1 | 300 MB |
| B2 | 200 MB |
| B3 | 100 MB |
| B4 | 400 MB |

### Processos

| Processo | Memória Necessária |
|----------|--------------------|
| P1 | 120 MB |
| P2 | 80 MB |
| P3 | 200 MB |
| P4 | 90 MB |
| P5 | 350 MB |

### Resultado esperado

```
P1 → Bloco 1
P2 → Bloco 1
P3 → Bloco 2
P4 → Bloco 4
P5 → Não alocado
```

---

## Cenário 5 — Best Fit

**Objetivo:** validar a alocação utilizando o algoritmo Best Fit.

### Blocos de memória

| Bloco | Tamanho |
|-------|----------|
| B1 | 300 MB |
| B2 | 200 MB |
| B3 | 100 MB |
| B4 | 400 MB |

### Processos

| Processo | Memória Necessária |
|----------|--------------------|
| P1 | 120 MB |
| P2 | 80 MB |
| P3 | 200 MB |
| P4 | 90 MB |
| P5 | 350 MB |

### Resultado esperado

```
P1 → Bloco 2
P2 → Bloco 3
P3 → Bloco 1
P4 → Bloco 1
P5 → Bloco 4
```

---

## Cenário 6 — Worst Fit

**Objetivo:** validar a alocação utilizando o algoritmo Worst Fit.

### Blocos de memória

| Bloco | Tamanho |
|-------|----------|
| B1 | 300 MB |
| B2 | 200 MB |
| B3 | 100 MB |
| B4 | 400 MB |

### Processos

| Processo | Memória Necessária |
|----------|--------------------|
| P1 | 120 MB |
| P2 | 80 MB |
| P3 | 200 MB |
| P4 | 90 MB |
| P5 | 350 MB |

### Resultado esperado

```
P1 → Bloco 4
P2 → Bloco 1
P3 → Bloco 4
P4 → Bloco 2
P5 → Não alocado
```

---

## Observações

- **FCFS:** executa os processos por ordem de chegada.
- **SJF:** executa primeiro o processo com menor tempo de CPU.
- **Prioridade:** executa primeiro o processo de maior prioridade (menor número).
- **First Fit:** utiliza o primeiro bloco de memória disponível que comporte o processo.
- **Best Fit:** utiliza o menor bloco de memória capaz de acomodar o processo.
- **Worst Fit:** utiliza o maior bloco de memória disponível.

Todos os cenários acima podem ser reproduzidos na interface do simulador para validar o funcionamento dos algoritmos implementados.

## Autor

Felipe Krause
