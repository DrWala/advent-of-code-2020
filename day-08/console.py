def parse(content):
    instructions = []
    for line in content:
        line = line.split(" ")
        instructions.append(line)
    
    return instructions

def solve(content):
    instructions = parse(content)
    
    acc = 0
    run_inst = {}
    idx = 0
    while True:
        if idx in run_inst:
            break

        inst = instructions[idx]
        
        if inst[0] == "nop":
            run_inst[idx] = True
            idx += 1
        elif inst[0] == "acc":
            run_inst[idx] = True
            acc += int(inst[1])
            idx += 1
        else:
            run_inst[idx] = True
            idx += int(inst[1])

    return acc

file = open("input.txt", "r")
print(f"Acc value before infinite loop: {solve(file.readlines())}")

