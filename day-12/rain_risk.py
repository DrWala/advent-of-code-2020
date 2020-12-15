def dir_to_cardinal(dir):
    if dir[0] != 0:
        if dir[0] == 1:
            return 'E'
        else:
            return 'W'
    else:
        if dir[1] == 1:
            return 'N'
        else:
            return 'S'

def cardinal_to_dir(cardinal):
    if cardinal == 'N':
        return [0, 1]
    elif cardinal == 'E':
        return [1, 0]
    elif cardinal == 'S':
        return [0, -1]
    else:
        return [-1, 0]

def rotate_right(cur):
    dirs = ['N', 'E', 'S', 'W']
    idx = dirs.index(cur)
    return dirs[(idx + 1) % len(dirs)]

def rotate_left(cur):
    dirs = ['N', 'E', 'S', 'W']
    idx = dirs.index(cur)
    return dirs[(idx - 1) % len(dirs)]

def rotate(cur, dir, deg):
    cardinal = dir_to_cardinal(cur)
    if dir == 'R':
        for i in range(int(deg / 90)):
            cardinal = rotate_right(cardinal)
        return cardinal_to_dir(cardinal)
    else:
        for i in range(int(deg / 90)):
            cardinal = rotate_left(cardinal)
        return cardinal_to_dir(cardinal)

def manhattan(x_vectors, y_vectors):
    dist = 0
    return abs(sum(x_vectors)) + abs(sum(y_vectors))

def solve(content):
    content = [[line.strip()[0], line.strip()[1:]] for line in content]
    #      X  Y
    dir = [1, 0]
    x_vectors = []
    y_vectors = []

    for inst in content:
        inst[1] = int(inst[1])
        if inst[0] == 'N':
            tmp = dir[:]
            dir[1] = 1
            x_vectors.append(0 * dir[0])
            y_vectors.append(inst[1] * dir[1])
            dir = tmp[:]
        elif inst[0] == 'S':
            tmp = dir[:]
            dir[1] = -1
            x_vectors.append(0 * dir[0])
            y_vectors.append(inst[1] * dir[1])
            dir = tmp[:]
        elif inst[0] == 'E':
            tmp = dir[:]
            dir[0] = 1
            x_vectors.append(inst[1] * dir[0])
            y_vectors.append(0 * dir[1])
            dir = tmp[:]
        elif inst[0] == 'W':
            tmp = dir[:]
            dir[0] = -1
            x_vectors.append(inst[1] * dir[0])
            y_vectors.append(0 * dir[1])
            dir = tmp[:]
        elif inst[0] == 'F':
            x_vectors.append(inst[1] * dir[0])
            y_vectors.append(inst[1] * dir[1])
        elif inst[0] == 'R' or inst[0] == 'L':
            dir = rotate(dir, inst[0], inst[1])[:]
    
    return manhattan(x_vectors, y_vectors)


file = open("input.txt", "r")
content = file.readlines()
dist = solve(content)
print(f"Manhattan distance = {dist}")