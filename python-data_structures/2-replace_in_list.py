#!/usr/bin/python3
#2-replace_in_list.py
#Julio Perez <9034@holbertonstudents.com>

def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list