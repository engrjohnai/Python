def convert_cel_to_far(temp_cel):
    temp_far = float(temp_cel) * ( 9 / 5 ) + 32
    return round(temp_far, 2)
    
def convert_far_to_cel (temp_far):
    temp_cel = float(temp_far - 32 ) * 5 / 9
    return round(temp_cel, 2)


conversion_type = input("what is the conversion type: ? \nEnter 'A' if celcius to fahrenheit\nEnter 'B' if fahrenheit to celcius\n: ")
conversion_type = conversion_type.lower()


if conversion_type == "a":
    temp_cel = (input("Enter your temperature in celcius: "))
    try:
        temp_far = convert_cel_to_far(temp_cel)
        print(f"The temperature in celcius {temp_cel} is equivalent to {temp_far} in Farenheit")
    except ValueError:
        print("Please enter a valid numeric value for the temperature.")
    

elif conversion_type == "b":
    temp_far = (input("Enter your temperature in farenheit: "))
    try:
        temp_cel = convert_far_to_cel(temp_far)
        print(f"The temperature in celcius {temp_far} equivalent to {temp_cel} in Celcius")
    except ValueError:
        print("Please enter a valid numeric value for the temperature.")

