
prices = {
    "Bubblegum": 202, 
    "Toffee": 118, 
    "Ice cream": 2250, 
    "Milk chocolate": 1680, 
    "Doughnut": 1075, 
    "Pancake": 80
    }

print("Earned amount: ")
for key, value in prices.items():
     print(f"{key}: ${value}")

income = 0
for key, value in prices.items():
    income = income + value
    income = float(income)
print("")
print(f"Income: ${income}")


print('This string\'s content is boring')
print("But this one contains an ASCII fish: ><((((\">")