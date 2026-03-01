def enrollment(average_grade, recommended_by_tutor, finished_introductory_course, introductory_course_grade):
    enroll_student = ((average_grade >= 40 and recommended_by_tutor) 
            or (finished_introductory_course and introductory_course_grade > 85))
    return enroll_student

average_grade = int(input("Enter average_grade: "))
recommended_by_tutor = bool(input("Is the student recomended by tutor? "))
finished_introductory_course = bool(input("Did the student finished introductory coursse? "))
introductory_course_grade = int(input("Enter recommended_by_tutor: "))


print(enrollment(average_grade, recommended_by_tutor, finished_introductory_course, introductory_course_grade))



num1 = int(input())
num2 = int(input())
num3 = int(input())

print(num3 > num2 > num1)


# Please don't modify this code
# `a` stores an input value
a = int(input().strip())

# put your code here
print(a > 0)



set_number = 6557

a = int(input())
b = int(input())

print(a * b == set_number)



# You can get the input number as follows
input_number = int(input())

# Write your if statement for number range here
if input_number >= 10 and input_number <= 20:
    print('Inside the range')
else:
    print('Outside the range')


age = int(input())
if age < 18:
    print("Minor")
elif "<=  18 age >= 64":
    print("Adult")
else:
    print("Senior")




num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(num1)
    print(num2)
elif num2 > num1:
    print(num2)
    print(num1)
else:
    print(num1)
    print(num2)



num = int(input())

if num < 0:
    num = num * -1
    print(num)
    print("The number is positive")
else:
    num = num * -1
    print(num)
    print("The number is negative")

x = 111
print(x * 3 if x <= 99988 else x * 2)



year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap")
else:
    print("Ordinary")


name = input()
print("Hello, world! Hello," + name)


word1 = "short"
word2 = "longer"
word3 = "longest"
def find_longest(word1, word2, word3):
    return max (len(word1), len(word2), len(word3))

print(find_longest)



digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers = input("Enter number here: ")

for char in numbers:
    index = int(char)
    name = digits[index]
    print(name)


string = "red yello fox bite orange goose beeeeeeeep"
vowels = ['a', 'e', 'i', 'o', 'u']
counter = 0

for char in string:
    if char.lower() in vowels:
        counter += 1
       
print(f"\nTotal vowels found: {counter}")


a = int(input())
b = int(input())
counter = 0
total = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        counter += 1
        total += i

average = total / counter
print(average)



x = int(input("Enter the King's x-cordinate: "))
y = int(input("Enter the King's y-cordinate: "))


if not (1 <= x <= 8 and 1 <= y <= 8):
    print("Invalid cordinates. Cordinates must between 1 and 8 inclusive")

valid_move_count = 0

possible_deltas = [
    (-1, -1), (0, -1), (1, -1), # Up-Left, Up, Up-Right
    (-1, 0),            (1, 0), # Left, Right
    (-1, 1), (0, 1), (1, 1) # Down-Left, Down, Down-Right
]

for dx, dy in possible_deltas:
    new_x = x + dx
    new_y = y + dy


    is_valid_x = 1 <= new_x <= 8
    is_valid_y = 1 <= new_y <= 8


    if is_valid_x and is_valid_y:
        valid_move_count += 1


print(valid_move_count)



num = int(input())

if num < 1:
    print("no army")
elif (1 <= num <= 9):
    print("few")
elif (10 <= num <= 49):
    print("pack")
elif (50 <= num <= 499):
    print("horde")
elif (500 <= num <= 999):
    print("swarm")
else:
    print("legion")