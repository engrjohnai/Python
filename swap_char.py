"""
Swapping first and last characters
Report a typo

Write a program that takes a string as input and returns the string with the first and last characters swapped. For example, if the input is "hello", the output should be "oellh".

Sample Input 1:

python

Sample Output 1:

nythop

Sample Input 2:

OpenAI

Sample Output 2:

IpenAO
"""
input_string = input()
def swap_first_last(string):
    first_char = string[0]
    middle_char = string[1:-1]
    last_char = string[-1]

    return last_char + middle_char + first_char


result = swap_first_last(input_string)
print(result)


'''
title = input()
print(title.upper())
'''

word = input()

result = word.strip('"*_~`"')
print(result)
