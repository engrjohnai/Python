"""
Calculate the arithmetic mean of integer numbers and output it. You will receive the integers on separate lines. The numeric sequence ends with a period ., so stop reading the input on it.

Don't round your result before outputting it.

The input will always have at least one number. 

"""

count = 0
sum = 0

while True:
    a = input()
    if a != ".":
        a = int(a)
        sum += a
        count += 1
    else:
        break
    

average = sum / count
print(average)
    