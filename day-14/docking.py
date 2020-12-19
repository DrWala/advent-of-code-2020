import re

def mask(mask, val):
    val = list(val)
    for idx, char in enumerate(mask):
        if char != 'X':
            val[idx] = char
    return ''.join(val)

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

            val_binary = mask(mask_str, bin(val)[2:].zfill(36))
            mem[mem_addr] = int(val_binary, 2)
    return sum(mem.values())


file = open("input.txt", "r")
program_input = file.readlines()
val_sum = solve(program_input)
print(f"sum of all values = {val_sum}")