#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if not list_of_integers:
        return None
    n = len(list_of_integers)    
    if n < 3:
        return max(list_of_integers)
    mid = n // 2
    if list_of_integers[mid] > list_of_integers[mid-1] and list_of_integers[mid] > list_of_integers[mid+1]:
        return list_of_integers[mid]
    else:
        left_peak = find_peak(list_of_integers[:mid])
        right_peak = find_peak(list_of_integers[mid:])
        return max(left_peak, right_peak)
