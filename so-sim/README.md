# SO-Sim

Simulador de Sistemas Operacionais desenvolvido em Python.

## Funcionalidades

### Escalonamento de CPU

* FCFS (First Come First Served)
* SJF (Shortest Job First)
* Round Robin
* Escalonamento por Prioridade

### Gerenciamento de Memória

* First Fit
* Best Fit
* Worst Fit

### Interface Gráficad

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
pip install -r requirements.txt
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

## Autor

Felipe Krause
