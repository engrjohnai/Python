

pizza = ["Margherita", "Four Seasons", "Neapolitan", "Vegetarian, Spicy"]
salad = ["Caesar salad", "Green salad", "Tuna salad", "Fruit salad"]
soup = ["Chicken soup", "Ramen", "Tomato soup", "Mushroom cream soup"]



x = input()
if x == "pizza":
    print(", ".join(pizza))
elif x == "salad":
    print(", ".join(salad))
elif x == "soup":
    print(", ".join(soup))
else:
    print("Sorry, we don't have it on the menu")