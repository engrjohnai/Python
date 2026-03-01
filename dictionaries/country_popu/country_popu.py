

d = {
    "china": 143,
     "india": 136,
     "usa": 32,
     "pakistan": 21 
   }

a = input("Enter either Print/Add/Remove/Query below: ").lower()

if a == 'print':
    for key, value in d.items():
        print(f"{key}==>{value}")

elif a == 'add':
    c_add = input("Enter the country name you want to add: ")
    if c_add in d:
        print("{c_add} already exist in dataset")
    else:
        c_add_p = int(input("Enter the countries Population: "))
        d[c_add] = c_add_p
        print(f'Updated Dictionary: {d}')

elif a == 'remove':
    a_remove = input("Enter the Country you will like to remove: ").lower()
    if a_remove in d:
        del d[a_remove]
        print(f"Updated Dictionary: {d}")
    else:
        print("Country does not exist in our dictionary!")

elif a == 'query':
    a_query = input('Enter the country you will like to Query: ')
    if a_query in d:
        print(f'The population of {a_query} is {d[a_query]}')
    else:
        print(f'{a_query} is not on the dictionary')



        