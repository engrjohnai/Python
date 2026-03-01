

import operator
catalog = {'green table': 5000, 'brown chair': 1500, 'blue sofa': 15000, 'wardrobe': 10000}

catalog_sorted_by_key = dict(sorted(catalog.items(), key=operator.itemgetter(0), reverse=True))
print(catalog_sorted_by_key)

student_list = {
    "English": ['Tim', 'Carl', 'Dean', 'Jane'],
    "Maths": ['Jane', 'Mike', 'Ann', 'Kate', 'Nick', 'Jenny'],
    "Chemistry": ['Tim', 'Carl', 'Dean']
}

most_popular = max(student_list, key=lambda subject: len(student_list[subject]))

print(most_popular)
'''
m = student_list['Maths']
e = student_list['English']
c = student_list['Chemistry']

len_c = len(c)
len_e = len(e)
len_m = len(m)

max_len = max(len_c, len_e, len_m)

for max in list_sorted:
    if len_c:
        print('Chemistry')
    elif len_e:
        print('English')
    else:
        print('Math')
'''