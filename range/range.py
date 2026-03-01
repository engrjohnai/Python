#for i in range (1, 11):
    #print(i)
    #print(i*i)

exp = [2340, 2500, 2100, 3100, 2980]
for i in range(len(exp)):
    print("Month:", (i+1), "Expense:" , exp[i])

total = 0
total = total + exp[i]
print(f"My total expense is {total}")


key_location = input("Enter where you think you might find the key: ")
locations = ["garage", "living Room", "chair", "closet"]
for i in locations:
    if i == key_location:
        print("key is found in ", i)
        break
    else:
        print("key not found in ", i)



for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i * i)


i=1
while i<=5:
    print(i)
    i += 1
        