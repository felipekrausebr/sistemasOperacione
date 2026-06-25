from src.process import Process
from src.scheduler import Scheduler
from src.memory import MemoryManager
from src.utils import (
    print_results,
    print_gantt_chart,
    print_memory_results,
    print_memory_statistics,
    calculate_averages,
    get_memory_statistics
)


DEFAULT_MEMORY_BLOCKS = [300, 200, 100, 400]


def create_processes():
    return [
        Process("P1", 0, 5, 2, 120),
        Process("P2", 1, 3, 1, 80),
        Process("P3", 2, 8, 3, 200),
    ]


def run_fcfs():
    processes = create_processes()
    gantt = Scheduler.fcfs(processes)

    print("\n=== FCFS ===")
    print_gantt_chart(gantt)
    print()
    print_results(processes)


def run_sjf():
    processes = create_processes()
    gantt = Scheduler.sjf(processes)

    print("\n=== SJF ===")
    print_gantt_chart(gantt)
    print()
    print_results(processes)


def run_round_robin():
    processes = create_processes()
    quantum = 2
    gantt = Scheduler.round_robin(processes, quantum)

    print(f"\n=== Round Robin | Quantum = {quantum} ===")
    print_gantt_chart(gantt)
    print()
    print_results(processes)


def run_priority():
    processes = create_processes()
    gantt = Scheduler.priority_scheduling(processes)

    print("\n=== Prioridade ===")
    print("Critério: menor número = maior prioridade")
    print_gantt_chart(gantt)
    print()
    print_results(processes)


def run_memory_algorithm(name, algorithm):
    processes = create_processes()
    manager = MemoryManager(DEFAULT_MEMORY_BLOCKS)

    allocations = algorithm(manager, processes)

    print(f"\n=== Gerenciamento de Memória: {name} ===")
    print(f"Blocos iniciais: {DEFAULT_MEMORY_BLOCKS}")

    print_memory_results(allocations, manager.memory_blocks)
    print_memory_statistics(allocations, manager.memory_blocks)


def run_first_fit():
    run_memory_algorithm(
        "First Fit",
        lambda manager, processes: manager.first_fit(processes)
    )


def run_best_fit():
    run_memory_algorithm(
        "Best Fit",
        lambda manager, processes: manager.best_fit(processes)
    )


def run_worst_fit():
    run_memory_algorithm(
        "Worst Fit",
        lambda manager, processes: manager.worst_fit(processes)
    )


def run_comparison():
    results = []

    algorithms = [
        ("FCFS", lambda p: Scheduler.fcfs(p)),
        ("SJF", lambda p: Scheduler.sjf(p)),
        ("Round Robin", lambda p: Scheduler.round_robin(p, 2)),
        ("Prioridade", lambda p: Scheduler.priority_scheduling(p)),
    ]

    for name, algorithm in algorithms:
        processes = create_processes()
        algorithm(processes)

        avg_wait, avg_turn = calculate_averages(processes)
        results.append((name, avg_wait, avg_turn))

    print("\n" + "=" * 50)
    print("COMPARAÇÃO DE ALGORITMOS")
    print("=" * 50)

    print(
        f"\n{'Algoritmo':<15}"
        f"{'Espera Média':<18}"
        f"{'Turnaround Médio'}"
    )

    print("-" * 50)

    for name, avg_wait, avg_turn in results:
        print(
            f"{name:<15}"
            f"{avg_wait:<18.2f}"
            f"{avg_turn:.2f}"
        )

    best_waiting = min(results, key=lambda item: item[1])
    best_turnaround = min(results, key=lambda item: item[2])

    print("-" * 50)
    print(f"Melhor espera média: {best_waiting[0]} ({best_waiting[1]:.2f})")
    print(f"Melhor turnaround médio: {best_turnaround[0]} ({best_turnaround[2]:.2f})")


def create_custom_processes():
    processes = []

    quantity = int(input("\nQuantos processos deseja criar? "))

    for i in range(quantity):
        print(f"\nProcesso P{i + 1}")

        arrival = int(input("Tempo de chegada: "))
        burst = int(input("Tempo de CPU (Burst Time): "))
        priority = int(input("Prioridade: "))
        memory = int(input("Memória necessária (MB): "))

        processes.append(
            Process(
                f"P{i + 1}",
                arrival,
                burst,
                priority,
                memory
            )
        )

    return processes


def run_custom_simulation():
    processes = create_custom_processes()

    print("\nEscolha o algoritmo:")
    print("1 - FCFS")
    print("2 - SJF")
    print("3 - Round Robin")
    print("4 - Prioridade")

    algorithm = input("\nOpção: ")

    if algorithm == "1":
        gantt = Scheduler.fcfs(processes)
    elif algorithm == "2":
        gantt = Scheduler.sjf(processes)
    elif algorithm == "3":
        quantum = int(input("Quantum: "))
        gantt = Scheduler.round_robin(processes, quantum)
    elif algorithm == "4":
        gantt = Scheduler.priority_scheduling(processes)
    else:
        print("Algoritmo inválido.")
        return

    print("\n=== RESULTADO ===")
    print_gantt_chart(gantt)
    print()
    print_results(processes)


def run_full_report():
    processes = create_processes()

    print("\nEscolha o algoritmo de CPU:")
    print("1 - FCFS")
    print("2 - SJF")
    print("3 - Round Robin")
    print("4 - Prioridade")

    cpu_option = input("\nOpção: ")

    if cpu_option == "1":
        Scheduler.fcfs(processes)
        cpu_name = "FCFS"
    elif cpu_option == "2":
        Scheduler.sjf(processes)
        cpu_name = "SJF"
    elif cpu_option == "3":
        Scheduler.round_robin(processes, 2)
        cpu_name = "Round Robin"
    elif cpu_option == "4":
        Scheduler.priority_scheduling(processes)
        cpu_name = "Prioridade"
    else:
        print("Opção inválida.")
        return

    avg_wait, avg_turn = calculate_averages(processes)

    manager = MemoryManager(DEFAULT_MEMORY_BLOCKS)

    print("\nEscolha o algoritmo de memória:")
    print("1 - First Fit")
    print("2 - Best Fit")
    print("3 - Worst Fit")

    mem_option = input("\nOpção: ")

    if mem_option == "1":
        allocations = manager.first_fit(processes)
        mem_name = "First Fit"
    elif mem_option == "2":
        allocations = manager.best_fit(processes)
        mem_name = "Best Fit"
    elif mem_option == "3":
        allocations = manager.worst_fit(processes)
        mem_name = "Worst Fit"
    else:
        print("Opção inválida.")
        return

    stats = get_memory_statistics(allocations, manager.memory_blocks)

    print("\n" + "=" * 45)
    print("RELATÓRIO COMPLETO DO SISTEMA")
    print("=" * 45)

    print(f"\nCPU: {cpu_name}")
    print(f"Memória: {mem_name}")

    print("\n--- RESULTADOS DE CPU ---")
    print(f"Espera média: {avg_wait:.2f}")
    print(f"Turnaround médio: {avg_turn:.2f}")

    print("\n--- RESULTADOS DE MEMÓRIA ---")
    print(f"Memória total: {stats['total_memory']} MB")
    print(f"Memória utilizada: {stats['allocated_memory']} MB")
    print(f"Memória livre: {stats['free_memory']} MB")
    print(f"Taxa de ocupação: {stats['occupancy_rate']:.2f}%")
    print(f"Processos alocados: {stats['allocated_processes']}")
    print(f"Processos rejeitados: {stats['rejected_processes']}")


def show_menu():
    print("\n" + "=" * 40)
    print("SO-Sim - Simulador de SO")
    print("=" * 40)

    print("1 - FCFS")
    print("2 - SJF")
    print("3 - Round Robin")
    print("4 - Prioridade")
    print("5 - Memória: First Fit")
    print("6 - Memória: Best Fit")
    print("7 - Memória: Worst Fit")
    print("8 - Comparar Algoritmos")
    print("9 - Cenário Personalizado")
    print("10 - Relatório Completo CPU + Memória")
    print("0 - Sair")


def main():
    while True:
        show_menu()

        option = input("\nEscolha uma opção: ")

        if option == "1":
            run_fcfs()
        elif option == "2":
            run_sjf()
        elif option == "3":
            run_round_robin()
        elif option == "4":
            run_priority()
        elif option == "5":
            run_first_fit()
        elif option == "6":
            run_best_fit()
        elif option == "7":
            run_worst_fit()
        elif option == "8":
            run_comparison()
        elif option == "9":
            run_custom_simulation()
        elif option == "10":
            run_full_report()
        elif option == "0":
            print("\nEncerrando...")
            break
        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    main()