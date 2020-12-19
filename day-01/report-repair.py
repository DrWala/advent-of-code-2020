def two_sum(numbers, target):
    number_set = set()
    number_list = []
    
    for number in numbers:
        val = int(number)
        number_set.add(val)
        number_list.append(val)

    number_1 = "x"
    number_2 = "x"
    for number in number_list:
        if target - number in number_set:
            number_1 = number
            number_2 = target - number
    
            print(f"Number 1: {number_1}")
            print(f"Number 2: {number_2}")
            print(f"multiple = {number_1 * number_2}")
            return (number_1, number_2)
    return None

file = open("input.txt", "r")
two_sum(file.readlines(), 2020)