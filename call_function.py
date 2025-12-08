"""
Double greeting
Report a typo

We wrote a function that greets two people:

def greeting(first_name, second_name):
    print("Hello,", first_name, "and", second_name)

The first name is already stored in the variable first_name, and the second is stored in the variable second_name. Your task is to call this function twice in the code section. The first time it should print Hello, first_name and second_name, and the second time Hello, second_name and first_name.

Sample Input 1:

Sid
Nancy

Sample Output 1:

Hello, Sid and Nancy
Hello, Nancy and Sid
"""
# the following lines read names from the input, do not modify it, please
name_1 = input()
name_2 = input()

# your code here

def greeting(name_1, name_2):
    print(f"Hello, {name_1} and {name_2}")
    print(f"Hello, {name_2} and {name_1}")
          

greeting(name_1, name_2)
