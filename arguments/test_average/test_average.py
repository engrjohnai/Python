
def average_mark(*args):
    total = 0
    number = len(args)
    for n in args:
        total += n
    average = total / number
    return round(average, 1)


result = average_mark(3, 4, 5, 3)
print(result)

