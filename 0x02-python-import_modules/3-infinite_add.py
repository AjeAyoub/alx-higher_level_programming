#!/usr/bin/python3
'''program that prints the result of the addition of all arguments'''
if __name__ == "__main__":
    import sys
    numbers = sys.argv
    count_numbers = len(numbers) - 1
    result = 0

    for i in range(count_numbers):
        i += 1
        result = result +  int(numbers[i])
    print("{}".format(result))
