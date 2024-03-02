#!/usr/bin/python3
# function that finds a peak in a list of unsorted integers.

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    def recursive_peak(start, end):
        mid = (start + end) // 2

        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]

        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            return recursive_peak(start, mid - 1)
        else:
            return recursive_peak(mid + 1, end)

    return recursive_peak(0, len(list_of_integers) - 1)
