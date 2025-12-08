"""
simple interest calculation


Below you can find a simple program that performs simple interest calculation. The part that asks a user for the needed data has already been written for you. Now you need to write the final parts that will do all the heavy lifting:

    calculate() should perform interest calculation and return the final interest amount and the total sum.
    print_result() should print out the final interest amount and the total sum, as shown in the Sample Output below.

Here is the formula for calculating the interest: interest=amount×interest  rate×time100interest=100amount×interestrate×time​

In the Sample Input below, the first number is the starting amount, followed by the interest rate in % and the number of years.

You do NOT need to call the functions, just complete them!

Sample Input 1:

1000
8
5

Sample Output 1:

The interest is: 400.0
The total amount is: 1400.0
"""

amount = int(input("Enter the Initial Amount: "))
interest_rate = int(input("Enter the interest rate: "))
time = int(input("Enter the number of years: "))


def calculate(amount, interest_rate, time):
    interest = (amount * interest_rate * time) / 100
    total_amount = amount + interest
    return interest, total_amount


def print_result(interest, total_amount):
    total_amount = float(total_amount)
    interest = float(interest)
    print(f"The interest is: {interest}")
    print(f"The total amount is: {total_amount}")

interest, total_amount = calculate(amount, interest_rate, time)
print_result(interest, total_amount)