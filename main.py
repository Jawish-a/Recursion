numbers = [
    [1, 2, 3, 4],
    [3, 6, [5, 6], 8, 2,[2, 4], 9],
    [4, 2, [6, 7, [2, 6, 1]]]
]
def calculate_func(lst):
    sum = 0
    for i in lst:
        if(type(i) is int):
            sum += i
        else:
            sum += calculate_func(i)
    return sum
            

print(calculate_func(numbers))
