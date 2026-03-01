

def range_sum(numbers, start, end):
    current_sum = 0
    for x in numbers:
        if start <= x <= end:
            current_sum += x
    return current_sum

input_numbers_str = input()
try:
    input_numbers = [int(x) for x in input_numbers_str.split()]
except ValueError:
    input_numbers = []

try:
    a, b = map(int, input().split())
except ValueError:
    a, b = 0, 0 

print(range_sum(input_numbers, a, b))