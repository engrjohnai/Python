"""
Menu
Report a typo

Let's say you were asked to create a program for a restaurant: a visitor enters what kind of food they would like to order and gets back the restaurant's offer.

The restaurant has just opened so its menu contains only a few options:

    pizza: Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy
    salad: Caesar salad, Green salad, Tuna salad, Fruit salad
    soup: Chicken soup, Ramen, Tomato soup, Mushroom cream soup

If the visitors ask for something that is not on the menu, the program should write "Sorry, we don't have it on the menu".

Input: "pizza"
Output: "Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy"

Input: "burger"
Output: "Sorry, we don't have it on the menu"
"""

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