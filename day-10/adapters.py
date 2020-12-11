from collections import defaultdict

def solve(content):
    adapters = sorted([int(num) for num in content])
    diff = defaultdict(int)
    diff[3] = 1
    diff[adapters[0]] = 1
    for i in range(1, len(adapters)):
        diff[adapters[i] - adapters[i - 1]] += 1

    return diff[1] * diff[3]

def solve_two(content):
    adapters = sorted([int(num) for num in content])
    def count_valid(arr):
        i, j = 0
        
        ret = []
        arr_len = len(arr)
        if arr_len == 1:
            ret.append(0)
        if arr_len >= 2:
            if abs(arr[-2] - arr[-1]) <= 3:
                ret.append(arr_len - 1)
        
        if arr_len >= 3:
            if abs(arr[-3] - arr[-1]) <= 3:
                ret.append(arr_len - 2)
        
        if arr_len >= 4:
            if abs(arr[-4] - arr[-1]) <= 3:
                ret.append(arr_len - 3)

        return ret
    def count_ways(adapters):
        result = [1]
        for i in range(1, len(adapters) + 1):
            valid_past_indices = count_valid(adapters[:i])
            sum = 0
            for past_idx in valid_past_indices:
                sum += result[past_idx]
            result.append(sum)
        
        return result
    
    return count_ways(adapters)[-1]



        


file = open("input.txt", "r")
content = file.readlines()
print(f"Difference multiple = {solve(content)}")
print(f"Adapter combinations = {solve_two([0, 1, 2, 4, 5, 6, 9])}")