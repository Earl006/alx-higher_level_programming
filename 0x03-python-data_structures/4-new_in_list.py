#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(mylist):
        return (my_list)
    else:
        newList = my_list.copy()
        newList[idx] = element
        return (newList)
