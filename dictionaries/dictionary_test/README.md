my_dict = {'a': 1, 'b': 2, 'c': 3}
key, value = input().split()
value = int(value)
my_dict.update({key:value})

print(my_dict)