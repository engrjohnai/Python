items = ["bread", "pasta", "fruits", "veggies"]
print(items)
print(items[-2:])

items[0] = "chips"
print(items)
print(items[:-2])

items.append("butter")
print(items)

items.insert(1, "sugar")
print(items)


drinks = [" water", "soap", "soda", "coke" ]

shopping_list = items + drinks
print(shopping_list)

print(len(shopping_list))

print("bread" in items)