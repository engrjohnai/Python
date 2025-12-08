india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city_name = input("Enter a City Name: ")

if city_name in india:
    print(f"{city_name} is located in India")
elif city_name in pakistan:
    print(f"{city_name} is located in Pakistan")
elif city_name in bangladesh:
    print(f"{city_name} is in Bangladesh")
else:
    print("You have provided a city name that is not on the list")

