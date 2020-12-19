import re
from queue import Queue

def mask(mask, val):
    val = list(val)
    for idx, char in enumerate(mask):
        if char == '1':
            val[idx] = char
        elif char == 'X':
            val[idx] = 'X'
    
    addrQ = Queue()
    addrQ.put(val)
    all_variants = []
    while not addrQ.empty():
        possible_addr = addrQ.get()
        for idx, char in enumerate(possible_addr):
            if char == 'X':
                copied_zero = possible_addr[:]
                copied_one = possible_addr[:]
                copied_zero[idx] = 0
                copied_one[idx] = 1
                addrQ.put(copied_zero)
                addrQ.put(copied_one)
                break
        else:
            all_variants.append("".join([str(i) for i in possible_addr]))
    return all_variants

def solve(program_input):
    mask_str = ''
    mem = {}
    pattern = re.compile(r'((?<=mem\[)\d+(?=\])).+((?<= \= )\d+)')
    for line in program_input:
        line = line.strip()
        if line.split(' ')[0] == 'mask':
            mask_str = line[7:]
        else:
            match = pattern.search(line)
            mem_addr = int(match.group(1))
            val = int(match.group(2))
            mem_variants = mask(mask_str, bin(mem_addr)[2:].zfill(36))
            for mem_variant in mem_variants:
                mem[int(mem_variant, 2)] = val
    return sum(mem.values())


file = open("input.txt", "r")
program_input = file.readlines()
val_sum = solve(program_input)
print(f"sum of all values = {val_sum}")