

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
    