#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    numbers = sys.argv
    count_numbers = len(numbers) - 1
    result = 0

    for i in range(count_numbers):
        result = result +  int(numbers[i + 1])
    print("{}".format(result))
