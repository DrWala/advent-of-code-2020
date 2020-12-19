import re

def print_arr(arr):
    for entry in arr:
        print(entry)

def extract_valid_ranges(range_info):
    pattern = re.compile(r'\d+-\d+')
    valid_range_values = set()
    for line in range_info:
        for match in pattern.findall(line):
            valid_range = [int(i) for i in match.split('-')]
            for i in range(valid_range[0], valid_range[1] + 1):
                valid_range_values.add(i)
    return valid_range_values

def solve(content):
    valid_range_values = extract_valid_ranges(content[:20])
    error_rate = 0
    for other_ticket in content[25:]:
        other_ticket_values = [int(i) for i in other_ticket.split(",")]
        for val in other_ticket_values:
            if val not in valid_range_values:
                error_rate += val
    return error_rate

file = open("input.txt", "r")
content = file.readlines()
output = solve_two(content)
print(f"Error rate is {output}")

