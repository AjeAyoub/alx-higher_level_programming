#!/usr/bin/python3
# 3-print_alphabt.py

for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) not in ['q', 'e']:
        print("{}".format(chr(letter)), end='')
