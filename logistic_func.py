"""
Logistic function
Report a typo

Write a program that reads an integer and calculates the value of its logistic function. A logistic function, or sigmoid function, is a function defined by the formula σ(x)=11+e−x=exex+1σ(x)=1+e−x1​=ex+1ex​.

Print the result rounded to 2 decimal places.

You can use math.e constant equal to 2.718281… or sort of a shortcut math.exp(x) function, which is considered more accurate than math.e ** x or pow(math.e, x).

Sample Input 1:

95

Sample Output 1:

1.0

"""

import math

x = float(input())
solution = pow(math.e, x) / (pow(math.e, x) + 1)

solution = round(solution, 2)
print(solution)




