def print_map(seat_map):
    for row in seat_map:
        print(row)

def count_occupied_seats(seat_map):
    count = 0
    for row in seat_map:
        for seat in row:
            if seat == '#':
                 count += 1
    return count

def get_neighbours(seat_map, coords):
    neighbours = []
    r, c = coords
    move = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    cur_seat = seat_map[coords[0]][coords[1]]
    for i in range(8):
        coord = [r + move[i][0], c + move[i][1]]
        if 0 <= coord[0] <= len(seat_map) - 1 \
            and 0 <= coord[1] <= len(seat_map[0]) - 1 \
            and seat_map[coord[0]][coord[1]] == '#':
            
            neighbours.append(coord)

    return neighbours


def move_one_iteration(seat_map):
    did_we_change = False
    copy = [row[:] for row in seat_map]
    for ridx, row in enumerate(seat_map):
        for cidx, seat in enumerate(row):
            if seat != '.':
                neighbours = get_neighbours(seat_map, (ridx, cidx))
                # If we are dealing with a free seat, rule 1
                if seat == 'L':
                    if len(neighbours) == 0:
                        copy[ridx][cidx] = '#'
                        did_we_change = True
                elif seat == '#':
                    if len(neighbours) >= 4:
                        copy[ridx][cidx] = 'L'
                        did_we_change = True
    return (copy, did_we_change)

def solve(content):
    seat_map = [list(row.strip()) for row in content]
    while True:
        seat_map, did_we_change = move_one_iteration(seat_map)
        if did_we_change is False:
            break
    return count_occupied_seats(seat_map)

file = open("input.txt", "r")
content = file.readlines()
no_occupied = solve(content)
print(f"Number of occupied seats = {no_occupied}")