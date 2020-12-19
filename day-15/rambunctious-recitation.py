from collections import defaultdict

def solve(content):
    starting_numbers = [int(i) for i in content.split(",")]
    # Dict containing the turns at which a number was first spoken
    mem = defaultdict(list)
    for idx, num in enumerate(starting_numbers, 1):
        mem[num].append(idx)
    
    prev = starting_numbers[-1]
    for turn in range(len(starting_numbers) + 1, 30000001):
        # Has been spoken only ONCE before AND  was spoken on the literal previous turn
        if len(mem[prev]) == 1 and mem[prev][-1] == turn - 1:
            mem[0].append(turn)
            prev = 0
        elif len(mem[prev]) > 1:
            diff = abs(mem[prev][-1] - mem[prev][-2])
            mem[diff].append(turn)
            prev = diff
        else:
            mem[0].append(turn)
            prev = 0
    return prev

                


file = open("input.txt", "r")
content = file.readline()
output = solve(content)
print(f"The 2020th number spoken is {output}")