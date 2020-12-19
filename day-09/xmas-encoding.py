from collections import deque  

def check_valid_two_sum(number_set, target):
    for prev in set(number_set):
        if (target - prev) in number_set:
            return True
    return False

def solve_one(input):
    numbers = deque()
    limit = 25
    # set up till limit
    for idx, num in enumerate(input):
        if idx >= limit:
            break
        num = int(num)
        numbers.append(num)
    
    for num in input[limit:]:
        num = int(num)
        if not check_valid_two_sum(numbers, num):
            return num
        else:
            numbers.popleft()
            numbers.append(num)

def solve_two(input, target):
    input = [int(num) for num in input]
    total_sum, i, j, input_length = 0, 0, 1, len(input)
    while i < input_length and j < input_length:
        total_sum = sum(input[i:j])
        if total_sum < target:
            j += 1
        elif total_sum > target:
            i += 1
        else:
            return max(input[i:j]) + min(input[i:j])
    

    


file = open("input.txt", "r")
content = file.readlines()
incorrect = solve_one(content)
print(f"First value that does not follow the pattern is {incorrect}")
weakness = solve_two(content, incorrect)
print(f"Weakness is {weakness}")