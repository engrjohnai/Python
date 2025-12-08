"""
Calculate the factorial of a given number
Report a typo

Several number sequences exist in mathematics. One you might have heard of is Fibonacci series. 
Another one is the factorial sequence. Python provides the math module, which contains functions for mathematical operations. 
Your task is to calculate the factorial of the number given as input using the factorial function provided by the math module. 
Input: A single integer n (0 <= n <= 10). Output: Print the factorial of the given number.

Sample Input 1:

5

Sample Output 1:

120

Sample Input 2:

0

Sample Output 2:

1
"""

import math


n = int(input())

if (0 <= n <= 10):
    result = math.factorial(n)
    print(result)

else:
    print("Enter a number within the range (0 <= n <= 10)")



# place `import` statement at top of the program
import string

# don't modify this code or the variable may not be available
input_string = input()

# use capwords() here
result = string.capwords(input_string)


print(result)

