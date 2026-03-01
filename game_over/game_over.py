

scores = input().split()

mistake = "I"
correct = "C"
correct_count = 0
mistake_count = 0


for char in scores:
    if char == "I":
        mistake_count += 1
    else:
        correct_count += 1

    if mistake_count == 3:
        break

if mistake_count == 3:
    print("Game over")
else:
    print("You won")
    print(correct_count)

