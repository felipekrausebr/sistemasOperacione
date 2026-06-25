class Process:
    """
    Representa um processo dentro do simulador.

    A classe armazena os dados de entrada do processo e também
    os resultados calculados pelos algoritmos de escalonamento.
    """

    def __init__(self, pid, arrival_time, burst_time, priority=0, memory_required=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.memory_required = memory_required

        self.remaining_time = burst_time
        self.start_time = None
        self.finish_time = None
        self.waiting_time = 0
        self.turnaround_time = 0

    def __repr__(self):
        return (
            f"Process(pid={self.pid}, arrival_time={self.arrival_time}, "
            f"burst_time={self.burst_time}, priority={self.priority}, "
            f"memory_required={self.memory_required})"
        )