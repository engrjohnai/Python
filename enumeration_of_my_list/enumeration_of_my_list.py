
def find_my_list(all_lists, my_list):
    for index, lst in enumerate(all_lists):
        if id(lst) == id(my_list):
            return index