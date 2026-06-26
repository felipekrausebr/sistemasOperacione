import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.process import Process
from src.scheduler import Scheduler
from src.memory import MemoryManager
from src.utils import calculate_averages, get_memory_statistics


st.set_page_config(page_title="SO-Sim", page_icon="💻", layout="wide")

st.title("SO-Sim")
st.subheader("Simulador de Sistemas Operacionais")

tab_cpu, tab_memory, tab_dashboard = st.tabs([
    "Escalonamento de CPU",
    "Gerenciamento de Memória",
    "Dashboard"
])


def build_processes(processes_data):
    return [
        Process(
            item["pid"],
            item["arrival"],
            item["burst"],
            item["priority"],
            item["memory"]
        )
        for item in processes_data
    ]


def render_process_inputs():
    st.header("Configuração dos Processos")

    num_processes = st.number_input(
        "Quantidade de processos",
        min_value=1,
        max_value=10,
        value=3
    )

    processes_data = []

    for i in range(num_processes):
        st.subheader(f"Processo P{i + 1}")

        col1, col2 = st.columns(2)

        with col1:
            arrival = st.number_input(
                f"Chegada P{i + 1}",
                min_value=0,
                value=i,
                key=f"arrival_{i}"
            )

            burst = st.number_input(
                f"CPU P{i + 1}",
                min_value=1,
                value=5,
                key=f"burst_{i}"
            )

        with col2:
            priority = st.number_input(
                f"Prioridade P{i + 1}",
                min_value=1,
                value=i + 1,
                key=f"priority_{i}"
            )

            memory = st.number_input(
                f"Memória P{i + 1} (MB)",
                min_value=1,
                value=100,
                key=f"memory_{i}"
            )

        processes_data.append({
            "pid": f"P{i + 1}",
            "arrival": arrival,
            "burst": burst,
            "priority": priority,
            "memory": memory
        })

    return processes_data


with tab_cpu:
    processes_data = render_process_inputs()

    st.divider()

    algorithm = st.selectbox(
        "Escolha o algoritmo de escalonamento",
        ["FCFS", "SJF", "Prioridade"]
    )

    if st.button("Executar Simulação", key="executar_cpu"):
        processes = build_processes(processes_data)

        if algorithm == "FCFS":
            gantt = Scheduler.fcfs(processes)
        elif algorithm == "SJF":
            gantt = Scheduler.sjf(processes)
        else:
            gantt = Scheduler.priority_scheduling(processes)

        avg_wait, avg_turn = calculate_averages(processes)

        st.success("Simulação concluída.")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Espera média", f"{avg_wait:.2f}")

        with col2:
            st.metric("Turnaround médio", f"{avg_turn:.2f}")

        st.subheader("Tabela de processos")

        table_data = []

        for p in processes:
            table_data.append({
                "Processo": p.pid,
                "Chegada": p.arrival_time,
                "CPU": p.burst_time,
                "Prioridade": p.priority,
                "Memória": p.memory_required,
                "Início": p.start_time,
                "Fim": p.finish_time,
                "Espera": p.waiting_time,
                "Turnaround": p.turnaround_time
            })

        st.dataframe(pd.DataFrame(table_data), use_container_width=True)

        st.subheader("Gráfico de Gantt")

        gantt_data = []

        for pid, start, end in gantt:
            gantt_data.append({
                "Processo": pid,
                "Início": start,
                "Duração": end - start
            })

        df = pd.DataFrame(gantt_data)

        fig, ax = plt.subplots(figsize=(10, 4))

        for _, row in df.iterrows():
            ax.barh(
                row["Processo"],
                row["Duração"],
                left=row["Início"]
            )

            ax.text(
                row["Início"] + row["Duração"] / 2,
                row["Processo"],
                row["Processo"],
                ha="center",
                va="center",
                fontsize=10,
                bbox=dict(
                    facecolor="white",
                    alpha=0.7,
                    edgecolor="none"
                )
            )

        ax.set_xlabel("Tempo")
        ax.set_ylabel("Processo")
        ax.set_title(f"Gráfico de Gantt - {algorithm}")

        st.pyplot(fig)


with tab_memory:
    st.header("Gerenciamento de Memória")

    st.info(
        "Os processos utilizados aqui são os mesmos configurados na aba "
        "'Escalonamento de CPU'. Altere a memória de P1, P2, P3 etc. nessa aba."
    )

    memory_algorithm = st.selectbox(
        "Escolha o algoritmo de memória",
        ["First Fit", "Best Fit", "Worst Fit"]
    )

    st.subheader("Blocos de memória")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        block1 = st.number_input("Bloco 1 (MB)", min_value=1, value=300)

    with col2:
        block2 = st.number_input("Bloco 2 (MB)", min_value=1, value=200)

    with col3:
        block3 = st.number_input("Bloco 3 (MB)", min_value=1, value=100)

    with col4:
        block4 = st.number_input("Bloco 4 (MB)", min_value=1, value=400)

    memory_blocks = [block1, block2, block3, block4]

    st.write(f"Blocos configurados: {memory_blocks}")

    st.subheader("Processos utilizados na alocação")

    process_preview = []

    for item in processes_data:
        process_preview.append({
            "Processo": item["pid"],
            "Memória necessária (MB)": item["memory"]
        })

    st.dataframe(pd.DataFrame(process_preview), use_container_width=True)

    if st.button("Executar Alocação de Memória", key="executar_memoria"):
        processes = build_processes(processes_data)
        manager = MemoryManager(memory_blocks)

        if memory_algorithm == "First Fit":
            allocations = manager.first_fit(processes)
        elif memory_algorithm == "Best Fit":
            allocations = manager.best_fit(processes)
        else:
            allocations = manager.worst_fit(processes)

        stats = get_memory_statistics(allocations, manager.memory_blocks)

        st.success("Alocação concluída.")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Memória total", f"{stats['total_memory']} MB")

        with col2:
            st.metric("Memória utilizada", f"{stats['allocated_memory']} MB")

        with col3:
            st.metric("Memória livre", f"{stats['free_memory']} MB")

        col4, col5 = st.columns(2)

        with col4:
            st.metric("Taxa de ocupação", f"{stats['occupancy_rate']:.2f}%")

        with col5:
            st.metric("Processos rejeitados", stats["rejected_processes"])

        st.subheader("Tabela de alocação")

        allocation_data = []

        for item in allocations:
            allocation_data.append({
                "Processo": item["process"],
                "Memória necessária": item["memory_required"],
                "Bloco": (
                    "Não alocado"
                    if item["block_index"] is None
                    else item["block_index"]
                ),
                "Tamanho original": item["original_block_size"],
                "Sobra": item["remaining_block_size"]
            })

        st.dataframe(pd.DataFrame(allocation_data), use_container_width=True)

        st.subheader("Blocos livres após alocação")

        blocks_data = []

        for index, block in enumerate(manager.memory_blocks):
            blocks_data.append({
                "Bloco": index,
                "Memória livre": block
            })

        st.dataframe(pd.DataFrame(blocks_data), use_container_width=True)


with tab_dashboard:
    st.header("Dashboard do Sistema")

    total_cpu = sum(item["burst"] for item in processes_data)
    total_memory = sum(item["memory"] for item in processes_data)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Processos", len(processes_data))

    with col2:
        st.metric("CPU Total", total_cpu)

    with col3:
        st.metric("Memória Total", f"{total_memory} MB")

    st.divider()

    st.subheader("Resumo dos Processos")

    dashboard_data = []

    for item in processes_data:
        dashboard_data.append({
            "Processo": item["pid"],
            "Chegada": item["arrival"],
            "CPU": item["burst"],
            "Prioridade": item["priority"],
            "Memória": item["memory"]
        })

    st.dataframe(pd.DataFrame(dashboard_data), use_container_width=True)

    st.divider()

    st.subheader("Distribuição de Memória")

    fig, ax = plt.subplots()

    labels = [p["pid"] for p in processes_data]
    values = [p["memory"] for p in processes_data]

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    ax.set_title("Distribuição de Memória dos Processos")

    st.pyplot(fig)
