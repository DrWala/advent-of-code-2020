import re
from collections import defaultdict

def print_arr(arr):
    for entry in arr:
        print(entry)

# Gives us a dict of field => set of valid ranges
def extract_valid_ranges_by_key(range_info):
    pattern = re.compile(r'([a-z ]+): (\d+-\d+) or (\d+-\d+)')
    valid_range_values = defaultdict(set)
    for line in range_info:
        matches = list(pattern.findall(line)[0])
        for idx, match in enumerate(matches):
            # pattern.findall(0) should be the name of the field
            if idx != 0:
                valid_range = [int(i) for i in match.split('-')]
                for i in range(valid_range[0], valid_range[1] + 1):
                    # add all the valid values to the relevant field
                    valid_range_values[matches[0]].add(i)
    return valid_range_values

# Gives us a set of all possible range values so we can remove completely invalid ranges
def extract_valid_range_numbers(range_info):
    pattern = re.compile(r'\d+-\d+')
    valid_range_values = set()
    for line in range_info:
        for match in pattern.findall(line):
            valid_range = [int(i) for i in match.split('-')]
            for i in range(valid_range[0], valid_range[1] + 1):
                valid_range_values.add(i)
    return valid_range_values

def remove_invalid_tickets(tickets, valid_range_values):
    valid_tickets = []
    for ticket in tickets:
        for val in ticket:
            if val not in valid_range_values:
                break
        else:
            valid_tickets.append(ticket)
    
    return valid_tickets

def remove_item_from_all_vals(dict_to_remove_from, val):
    for arr in dict_to_remove_from.values():
        if val in arr:
            arr.remove(val)

def solve(content):
    valid_range_values = extract_valid_ranges_by_key(content[:20])
    valid_range_set = extract_valid_range_numbers(content[:20])
    
    range_index_map = defaultdict(list)

    # Convert to array for other tickets
    other_ticket_arr = []
    for other_ticket in content[25:]:
        other_ticket_arr.append([int(i) for i in other_ticket.split(",")])

    other_ticket_arr = remove_invalid_tickets(other_ticket_arr, valid_range_set)       
    
    cols = len(other_ticket_arr[0])

    # For each field, get the possible columns that work for it
    for key in valid_range_values.keys():
        # Check if col i works for current key
        for i in range(cols):
            for other_ticket in other_ticket_arr:
                if other_ticket[i] not in valid_range_values[key]:
                    break
            else:
                range_index_map[key].append(i)
    
    # Eliminate columns one by one
    final_correct_mapping = []
    for i in range(len(range_index_map)):
        for key, value in range_index_map.items():
            if len(value) == 1:
                final_correct_mapping.append((key, value[0]))
                remove_item_from_all_vals(range_index_map, value[0])


    prod = 1
    my_ticket = [int(i) for i in content[22].split(",")]
    for mapping in final_correct_mapping:
        if "departure" in mapping[0]:
            prod *= my_ticket[mapping[1]]
    
    return prod


file = open("input.txt", "r")
content = file.readlines()
output = solve(content)
print(f"Multiplication of fields with departure is {output}")

