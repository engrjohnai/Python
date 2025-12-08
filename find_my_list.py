"""
You play a game with your friends. You give them a non-empty list of integers and they create a list of lists, 
which contains your list and some other non-empty lists in some order. 
Your task is to find your list among other lists.

Complete the find_my_list(all_lists, my_list) function, 
where the first argument is the list of lists and the 
second argument is the list of integers that you should find. 
enumerate() is the built-in function, which takes an iterable and 
returns its elements one by one along with their indexes. 
The function should return the position of my_list in all_lists. 
The lists in all_lists are numbered from zero. It's guaranteed that an element exists in all_lists.

Tip: There can be other lists that contain the same values as your list. You should find exactly your list, not a copy of it.
"""

my_list = [0, 20, 1, 1, 22, 333, 454]
all_list = [2, 3, 4, 5, 6, 7, 8, 2, ]

enumerate(all_list)
print(enumerate(all_list))

def find_my_list(all_lists, my_list):
    for index, lst in enumerate(all_lists):
        # Change the next line
        print(index)
            


