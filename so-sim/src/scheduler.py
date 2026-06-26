class Scheduler:
    """
    Classe responsável pelos algoritmos de escalonamento de CPU.
    """

    @staticmethod
    def fcfs(processes):
        """
        First Come, First Served.

        Executa os processos na ordem de chegada.
        Algoritmo não preemptivo.
        """

        processes = sorted(processes, key=lambda p: p.arrival_time)

        current_time = 0
        gantt = []

        for process in processes:
            if current_time < process.arrival_time:
                current_time = process.arrival_time

            process.start_time = current_time
            process.waiting_time = process.start_time - process.arrival_time

            current_time += process.burst_time

            process.finish_time = current_time
            process.turnaround_time = process.finish_time - process.arrival_time

            gantt.append(
                (
                    process.pid,
                    process.start_time,
                    process.finish_time
                )
            )

        return gantt

    @staticmethod
    def sjf(processes):
        """
        Shortest Job First não preemptivo.

        A cada decisão, escolhe entre os processos já disponíveis
        aquele com menor tempo de CPU.
        """

        processes = processes.copy()
        completed = []
        gantt = []
        current_time = 0

        while len(completed) < len(processes):
            ready = [
                p for p in processes
                if p not in completed and p.arrival_time <= current_time
            ]

            if not ready:
                current_time += 1
                continue

            process = min(ready, key=lambda p: p.burst_time)

            process.start_time = current_time
            process.waiting_time = process.start_time - process.arrival_time

            current_time += process.burst_time

            process.finish_time = current_time
            process.turnaround_time = process.finish_time - process.arrival_time

            gantt.append(
                (
                    process.pid,
                    process.start_time,
                    process.finish_time
                )
            )

            completed.append(process)

        return gantt

    @staticmethod
    def priority_scheduling(processes):
        """
        Escalonamento por prioridade.

        Menor número significa maior prioridade.
        A escolha considera apenas processos que já chegaram.
        """

        processes = processes.copy()
        completed = []
        gantt = []
        current_time = 0

        while len(completed) < len(processes):
            ready = [
                p for p in processes
                if p not in completed and p.arrival_time <= current_time
            ]

            if not ready:
                current_time += 1
                continue

            process = min(ready, key=lambda p: p.priority)

            process.start_time = current_time
            process.waiting_time = process.start_time - process.arrival_time

            current_time += process.burst_time

            process.finish_time = current_time
            process.turnaround_time = process.finish_time - process.arrival_time

            gantt.append(
                (
                    process.pid,
                    process.start_time,
                    process.finish_time
                )
            )

            completed.append(process)

        return gantt
