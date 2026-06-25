class MemoryManager:
    """
    Classe responsável por simular algoritmos de alocação de memória.

    A memória é representada por uma lista de blocos livres.
    Cada número da lista representa o tamanho disponível de um bloco em MB.
    """

    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks.copy()
        self.allocations = []

    def first_fit(self, processes):
        """
        First Fit.

        Aloca o processo no primeiro bloco livre que tenha espaço suficiente.
        """

        for process in processes:
            chosen_index = None

            for index, block_size in enumerate(self.memory_blocks):
                if block_size >= process.memory_required:
                    chosen_index = index
                    break

            self._allocate(process, chosen_index)

        return self.allocations

    def best_fit(self, processes):
        """
        Best Fit.

        Aloca o processo no menor bloco livre que ainda tenha espaço suficiente.
        """

        for process in processes:
            best_index = None
            best_size = None

            for index, block_size in enumerate(self.memory_blocks):
                if block_size >= process.memory_required:
                    if best_size is None or block_size < best_size:
                        best_size = block_size
                        best_index = index

            self._allocate(process, best_index)

        return self.allocations

    def worst_fit(self, processes):
        """
        Worst Fit.

        Aloca o processo no maior bloco livre disponível.
        """

        for process in processes:
            worst_index = None
            worst_size = None

            for index, block_size in enumerate(self.memory_blocks):
                if block_size >= process.memory_required:
                    if worst_size is None or block_size > worst_size:
                        worst_size = block_size
                        worst_index = index

            self._allocate(process, worst_index)

        return self.allocations

    def _allocate(self, process, block_index):
        """
        Registra a alocação de um processo e atualiza o bloco de memória.

        Caso nenhum bloco seja suficiente, o processo é marcado como não alocado.
        """

        if block_index is None:
            self.allocations.append({
                "process": process.pid,
                "memory_required": process.memory_required,
                "block_index": None,
                "original_block_size": None,
                "remaining_block_size": None
            })
            return

        original_size = self.memory_blocks[block_index]
        remaining_size = original_size - process.memory_required

        self.allocations.append({
            "process": process.pid,
            "memory_required": process.memory_required,
            "block_index": block_index,
            "original_block_size": original_size,
            "remaining_block_size": remaining_size
        })

        self.memory_blocks[block_index] = remaining_size