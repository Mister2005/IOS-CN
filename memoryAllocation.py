def first_fit(memory, process):
    allocation = [-1] * len(process)
    block_used = [False] * len(memory)

    for i in range(len(process)):
        for j in range(len(memory)):
            if not block_used[j] and memory[j] >= process[i]:
                allocation[i] = j
                block_used[j] = True
                break
    return allocation

def best_fit(memory, process):
    allocation = [-1] * len(process)
    block_used = [False] * len(memory)

    for i in range(len(process)):
        best_index = -1
        min_diff = float('inf')

        for j in range(len(memory)):
            if not block_used[j] and memory[j] >= process[i]:
                diff = memory[j] - process[i]
                if diff < min_diff:
                    min_diff = diff
                    best_index = j

        if best_index != -1:
            allocation[i] = best_index
            block_used[best_index] = True
    return allocation

def worst_fit(memory, process):
    allocation = [-1] * len(process)
    block_used = [False] * len(memory)

    for i in range(len(process)):
        worst_index = -1
        max_diff = -1

        for j in range(len(memory)):
            if not block_used[j] and memory[j] >= process[i]:
                diff = memory[j] - process[i]
                if diff > max_diff:
                    max_diff = diff
                    worst_index = j

        if worst_index != -1:
            allocation[i] = worst_index
            block_used[worst_index] = True
    return allocation

def print_allocation(strategy_name, memory, process, allocation):
    print(f"\n{strategy_name} Allocation:")
    print("Process Size\tMemory Block")
    for i in range(len(process)):
        print(f"{process[i]}\t\t", end="")
        if allocation[i] != -1:
            print(memory[allocation[i]])
        else:
            print("Not Allocated")

def main():
    memory = []
    process = []

    blocks = int(input("Enter the number of memory blocks: "))
    for i in range(blocks):
        size = int(input(f"Block {i + 1} Size -> "))
        memory.append(size)

    processes = int(input("\nEnter the number of processes: "))
    for i in range(processes):
        size = int(input(f"Process {i + 1} Size -> "))
        process.append(size)

    print_allocation("First Fit", memory, process, first_fit(memory, process))
    print_allocation("Best Fit", memory, process, best_fit(memory, process))
    print_allocation("Worst Fit", memory, process, worst_fit(memory, process))

if __name__ == "__main__":
    main()