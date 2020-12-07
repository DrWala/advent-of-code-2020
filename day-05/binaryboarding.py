import math

def search_row(pattern):
    low = 0
    high = 127
    for char in list(pattern):
        # F is lower half
        if char == 'F':
            high = math.floor((high - low) / 2) + low
        elif char == 'B':
            low = math.ceil((high - low) / 2) + low
    
    return low

def search_seat(pattern):
    low = 0
    high = 7
    for char in list(pattern):
        # L is lower half
        if char == 'L':
            high = math.floor((high - low) / 2) + low
        elif char == 'R':
            low = math.ceil((high - low) / 2) + low
    
    return low

def solve_one(content):
    max = 0
    for line in content:
        line = line.strip()
        id = search_row(line[0:-3]) * 8 + search_seat(line[-3:])
        if id > max:
            max = id
    print(f"Highest seat id: {max}")

def solve_two(content):
    seats = []
    for line in content:
        line = line.strip()
        seats.append(search_row(line[0:-3]) * 8 + search_seat(line[-3:]))
    
    seats = sorted(seats)
    
    for idx in range(1, len(seats)):
        if not seats[idx] - 1 == seats[idx - 1]:
            print(f"Missing pass: {seats[idx] - 1}")

file = open("input.txt", "r")
content = file.readlines()
solve_one(content)
solve_two(content)

