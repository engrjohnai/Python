

word = input()
number_of_space = int(input())


print(*word, sep=' ' * number_of_space)


numbers = [int(x) for x in input().split()]
for number in numbers:
    print(number, end='')
print()



numbers = [int(x) for x in input().split()]
print(*numbers, sep='')