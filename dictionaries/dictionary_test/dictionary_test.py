planets = {'venus', 'earth', 'jupiter'}

#planets_dict = dict.fromkeys(planets)

#print(planets_dict)

value = 'planets'

planets_dict = dict.fromkeys(planets, value)
#print(planets_dict)


planets_dict['jupiter'] = "giant " + planets_dict['jupiter']

#print(planets_dict)


satellites = ['Moon', 'Io', 'Europa']
planets = {'Venus', 'Earth', 'Jupiter'}

planets_dict = dict.fromkeys(planets, satellites)

#print(planets_dict)

planets_dict['Earth'].append(satellites[0])
planets_dict['Jupiter'].append(satellites[1])
planets_dict['Jupiter'].append(satellites[2])
#print(planets_dict)  
# {'Jupiter': ['Moon', 'Io', 'Europa'], 'Venus': ['Moon', 'Io', 'Europa'], 'Earth': ['Moon', 'Io', 'Europa']}

planets_dict = {key: [] for key in planets}
#print(planets_dict)


testable = {'September': '16°C', 'December': '-10°C'} 
another_dictionary = {'June': '21°C'}

testable.update(another_dictionary)
#testable['June'] = '21°C'
testable.update(October='10°C')
#print(testable)


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merge_dict = dict1 | dict2

print(merge_dict)
"""
my_dict = {'a': 1, 'b': 2, 'c': 3}
key, value = input().split()
value = int(value)
my_dict.update({key:value})

print(my_dict)

"""

import operator
catalog = {'green table': 5000, 'brown chair': 1500, 'blue sofa': 15000, 'wardrobe': 10000}

catalog_sorted_by_key = dict(sorted(catalog.items(), key=operator.itemgetter(0), reverse=True))
print(catalog_sorted_by_key)