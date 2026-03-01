


def check_values(first_value, second_value):
    if bool(first_value and second_value):
        return True
    else:
        return False
    

result = check_values("a", "b")

print(result)