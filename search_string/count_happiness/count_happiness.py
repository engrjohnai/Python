

a = input()
b = input()
count = 0

to_count = a.split()

for word in to_count:
    if word == b:
        count += 1
        
print(count)