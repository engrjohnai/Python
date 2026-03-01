


def number_of_frogs(year):
    k = year
    if k == 1:
        return 120
    else:
        frogs_last_year = number_of_frogs(k - 1)
        fk = 2 * (frogs_last_year -50)
        return fk

result = number_of_frogs(5)
print(result)