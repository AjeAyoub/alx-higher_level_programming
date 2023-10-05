#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    count_arg = len(sys.argv) - 1

    if count_arg == 0:
        print("0 arguments.")
    elif count_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count_arg))
    for i in range(count_arg):
        print("{}: {}".format(i+1, sys.argv[i+1]))
