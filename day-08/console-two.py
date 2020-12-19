from collections import defaultdict
from queue import Queue

def create_graph(input):
    graph = defaultdict(list)
    instructions = []
    for idx, line in enumerate(input):
        line = line.strip().split(" ")
        instructions.append(line)
        graph[idx] = []
        neighbours = get_neighbour(line, idx)
        for n in neighbours:
            if n <= len(input):
                graph[idx].append(n)
    return (graph, instructions)

def get_neighbour(inst, idx):
    if inst[0] == "nop":
        return [idx + 1, idx + int(inst[1])]
    elif inst[0] == "acc":
        return [idx + 1]
    else:
        return [idx + 1, idx + int(inst[1])]

def solve(input):
    graph, instructions = create_graph(input)

    def bfs():
        run_inst = {}
        predecessor = {}
        queue = Queue()
        queue.put(0)
        run_inst[0] = True

        while not queue.empty():
            u = queue.get()
            if u == len(input):
                break
            inst = instructions[u]
            
            for neighbour in graph[u]:
                if neighbour not in run_inst:
                    run_inst[neighbour] = True
                    predecessor[neighbour] = u
                    queue.put(neighbour)    
        return predecessor
    
    predecessor = bfs()
    path = []
    v = max(graph.keys())
    while True:
        if v == 0:
            path.append(v)
            break
        path.append(v)
        v = predecessor[v]
    
    path = reversed(path)
    acc = 0
    for hop in path:
        inst = instructions[hop]
        if inst[0] == "acc":
                acc += int(inst[1])
    return acc

file = open("input.txt", "r")
print(f"Acc value after fixing infinite loop: {solve(file.readlines())}")

