

def sq_num(*args):
    total = 0
    for n in args:
        square = n * n
        total += square
    return total


result = sq_num(1, 10, 10)
print(result)