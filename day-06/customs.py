# Part 1
def count_valid_one(entry_str):
    entry_str = entry_str.replace('\n', '')
    return len(set(list(entry_str)))

def convert_file_to_group_forms(content):
    return content.split("\n\n")

def solve_one(content):
    group_forms = forms = convert_file_to_group_forms(content)
    count = 0
    for form in group_forms:
        count += count_valid_one(form)
    
    print(f"count = {count}")

# Part 2
def count_valid_two(entry_str):
    entries = [set(entry) for entry in entry_str.split('\n')]
    return len(set.intersection(*entries))

def solve_two(content):
    group_forms = forms = convert_file_to_group_forms(content)
    count = 0
    for form in group_forms:
        count += count_valid_two(form)
    
    print(f"count = {count}")

file = open("input.txt", "r")
content = file.read()
file.close()

solve_one(content)
solve_two(content)