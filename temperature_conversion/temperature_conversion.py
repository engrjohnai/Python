


def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)



def main():
    raw_input = input()
    temperature, unit = raw_input.split()
    temperature = int(temperature)
    if unit == "F":
        temps_f = temperature
        print(f"{fahrenheit_to_celsius(temps_f)} C")
    else:
        temps_c = temperature
        print(f"{celsius_to_fahrenheit(temps_c)} F")


main()