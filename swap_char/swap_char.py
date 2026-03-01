
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
