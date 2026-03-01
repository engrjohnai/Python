x = int(input("Enter any Positive integer here: "))
if x < 0:
    print(f"Your input {x} is not a positive integer")

for num in range(1, x + 1):
    if x % num == 0:
        print(f"{num} is a factor of {x}")
