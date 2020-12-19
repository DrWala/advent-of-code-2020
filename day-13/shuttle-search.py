import math

def solve(earliest, busses):
    earliest = int(earliest)
    busses = sorted([int(bus) for bus in busses.split(',') if bus.isdigit()])
    
    time = float("inf")
    bus_id = 0
    minint = math.floor(earliest / busses[-1])
    maxint = math.ceil(earliest / busses[0])
    for i in range(math.floor(earliest/busses[-1]), math.ceil(earliest / busses[0])):
        for bus in busses:
            if earliest <= bus * i <= time:
                time = bus * i
                bus_id = bus

    diff = time - earliest
    return diff * bus_id

file = open("input.txt", "r")
earliest = file.readline()
busses = file.readline()
bus_id = solve(earliest, busses)
print(f"ID * time = {bus_id}")