def print_results(processes):
    print("Processo | Chegada | CPU | Início | Fim | Espera | Turnaround")
    print("-" * 66)

    total_waiting = 0
    total_turnaround = 0

    for p in processes:
        total_waiting += p.waiting_time
        total_turnaround += p.turnaround_time

        print(
            f"{p.pid:^8} | "
            f"{p.arrival_time:^7} | "
            f"{p.burst_time:^3} | "
            f"{p.start_time:^6} | "
            f"{p.finish_time:^3} | "
            f"{p.waiting_time:^6} | "
            f"{p.turnaround_time:^10}"
        )

    print("-" * 66)
    print(f"Média de espera: {total_waiting / len(processes):.2f}")
    print(f"Média de turnaround: {total_turnaround / len(processes):.2f}")


def print_gantt_chart(gantt):
    print("\nGráfico de Gantt:")

    if not gantt:
        print("Nenhum processo executado.")
        return

    top_line = ""
    middle_line = ""
    time_line = "0"

    for item in gantt:
        pid, start, end = item
        duration = end - start

        block_width = max(7, duration * 3)

        top_line += "-" * block_width
        middle_line += f"|{pid:^{block_width - 1}}"
        time_line += f"{end:>{block_width}}"

    middle_line += "|"

    print(top_line)
    print(middle_line)
    print(top_line)
    print(time_line)


def print_memory_results(allocations, memory_blocks):
    print("\nResultado da alocação de memória:\n")
    print("Processo | Memória | Bloco | Tamanho original | Sobra")
    print("-" * 60)

    for item in allocations:
        if item["block_index"] is None:
            print(
                f"{item['process']:^8} | "
                f"{item['memory_required']:^7} | "
                f"{'N/A':^5} | "
                f"{'Não alocado':^16} | "
                f"{'N/A':^5}"
            )
        else:
            print(
                f"{item['process']:^8} | "
                f"{item['memory_required']:^7} | "
                f"{item['block_index']:^5} | "
                f"{item['original_block_size']:^16} | "
                f"{item['remaining_block_size']:^5}"
            )

    print("-" * 60)

    print("\nBlocos livres após alocação:")
    for index, block in enumerate(memory_blocks):
        print(f"Bloco {index}: {block} MB")


def calculate_averages(processes):
    avg_waiting = sum(p.waiting_time for p in processes) / len(processes)
    avg_turnaround = sum(p.turnaround_time for p in processes) / len(processes)

    return avg_waiting, avg_turnaround


def get_memory_statistics(allocations, memory_blocks):
    free_memory = sum(memory_blocks)

    allocated_memory = 0
    allocated_processes = 0
    rejected_processes = 0

    for item in allocations:
        if item["block_index"] is not None:
            allocated_memory += item["memory_required"]
            allocated_processes += 1
        else:
            rejected_processes += 1

    total_memory = free_memory + allocated_memory

    occupancy_rate = 0

    if total_memory > 0:
        occupancy_rate = (allocated_memory / total_memory) * 100

    return {
        "total_memory": total_memory,
        "allocated_memory": allocated_memory,
        "free_memory": free_memory,
        "occupancy_rate": occupancy_rate,
        "allocated_processes": allocated_processes,
        "rejected_processes": rejected_processes
    }


def print_memory_statistics(allocations, memory_blocks):
    stats = get_memory_statistics(allocations, memory_blocks)

    print("\n" + "=" * 30)
    print("ESTATÍSTICAS DE MEMÓRIA")
    print("=" * 30)

    print(f"Memória total:      {stats['total_memory']} MB")
    print(f"Memória utilizada:  {stats['allocated_memory']} MB")
    print(f"Memória livre:      {stats['free_memory']} MB")

    print(f"\nTaxa de ocupação: {stats['occupancy_rate']:.2f}%")

    print(f"\nProcessos alocados:   {stats['allocated_processes']}")
    print(f"Processos rejeitados: {stats['rejected_processes']}")
