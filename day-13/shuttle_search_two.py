from functools import reduce
def chinese_remainder(n, a):
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1

    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def solve(busses):
    busses = busses.split(',')
    # lets say x mod n = a
    # the values you modulo by, i.e n
    bus_list = []
    # the outcome of the module, i.e a
    indices = []
    for idx, item in enumerate(busses):
        if item.isdigit():
            bus_list.append(int(item))
            # Why does this work?
            indices.append(-idx % int(item))
    ret = chinese_remainder(bus_list, indices)
    return ret

file = open("input.txt", "r")
# skip the first line
file.readline()

busses = file.readline()
earliest = solve(busses)
print(f"earliest timestamp = {earliest}")