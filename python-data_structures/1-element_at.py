#usr/nin/env python3
#1-element_at.py
## Julio Perez <9034@holbertonschool.com>

def element_at(my_list, idx):
    if 0 <= idx < len(my_list):
        return my_list[idx]
    else:
        return None