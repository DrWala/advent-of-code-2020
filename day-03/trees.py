def count_trees(terrain, slope_right, slope_down):
    cur_r, cur_c = 0, 0
    terrain_count = 0
    width = len(terrain[0]) - 1
    while cur_r != len(terrain) - 1:
        cur_c = (cur_c + slope_right) % width
        cur_r += slope_down
        if terrain[cur_r][cur_c] == '#':
            terrain_count += 1
    return terrain_count

file = open("input.txt", "r")
lines = file.readlines()
one = count_trees(lines, 1, 1)
two = count_trees(lines, 3, 1)
three = count_trees(lines, 5, 1)
four = count_trees(lines, 7, 1)
five = count_trees(lines, 1, 2)

print(f"part 1: {two}")
print(f"part 2: {one * two * three * four * five}")