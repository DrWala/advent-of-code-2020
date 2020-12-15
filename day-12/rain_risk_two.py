def rotate_right(cur):
    return [cur[1], -cur[0]]

def rotate_left(cur):
    return [-cur[1], cur[0]]

def rotate(cur, dir, deg):
    if dir == 'R':
        for i in range(int(deg / 90)):
            cur = rotate_right(cur)
    else:
        for i in range(int(deg / 90)):
            cur = rotate_left(cur)
    return cur

def solve(content):
    content = [[line.strip()[0], line.strip()[1:]] for line in content]
    #      X  Y
    ship = [0, 0]
    waypoint = [10, 1]

    for inst in content:
        inst[1] = int(inst[1])
        if inst[0] == 'N':
            waypoint[1] += inst[1]
        elif inst[0] == 'S':
            waypoint[1] += inst[1]
        elif inst[0] == 'E':
            waypoint[0] += inst[1]
        elif inst[0] == 'W':
            waypoint[0] += -inst[1]
        elif inst[0] == 'F':
            ship[0] += waypoint[0] * inst[1]
            ship[1] += waypoint[1] * inst[1]
        elif inst[0] == 'R' or inst[0] == 'L':
            waypoint = rotate(waypoint, inst[0], inst[1])[:]
    
    return abs(ship[0]) + abs(ship[1])


file = open("input.txt", "r")
content = file.readlines()
dist = solve(content)
print(f"Manhattan distance = {dist}")