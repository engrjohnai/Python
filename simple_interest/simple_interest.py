

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