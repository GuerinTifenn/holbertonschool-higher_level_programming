#!/usr/bin/python3

def no_c(my_string):
    str_no_c = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            str_no_c += char
    return str_no_c
