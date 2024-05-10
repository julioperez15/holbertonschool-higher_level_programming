#!/usr/bin/python3
# 4-hidden_discovery.py
# Julio Perez <9034@holbertonschool.com>

if __name__ == "__main__":
    import hidden_4
    for name in dir(hidden_4):
        if name[0] != '_' and name[1] != '_':
            print(name)