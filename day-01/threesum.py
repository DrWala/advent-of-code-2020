from twosum import two_sum

def three_sum(numbers, target):
    number_set = set()
    number_list = []

    for number in numbers:
        val = int(number)
        number_set.add(val)
        number_list.append(val)
    
    for number in number_list:
        ret = two_sum(numbers, target - number)
        if ret is not None:
            print(f"Number 1: {number}")
            print(f"Number 2: {ret[0]}")
            print(f"Number 3: {ret[1]}")
            print(f"multiple = {number * ret[0] * ret[1]}")
            break



file = open("input.txt", "r")

three_sum(file.readlines(), 2020)