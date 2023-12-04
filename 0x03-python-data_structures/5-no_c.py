#!/usr/bin/python3

def no_c(my_string):
    updated =''
    for i in my_string:
        if i != 'c' or i != 'C':
            updated += i
            return (updated)
