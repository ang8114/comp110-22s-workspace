"""Where I implent function skeletons and implementations."""

__author__ = "730391695"


def only_evens(evens: list[int]) -> list:
    """Returns only even integers of the input parameter."""
    i: int = 0
    even: list[int] = []
    while i < len(evens):
        if evens[i] % 2 == 0:
            even.append(evens[i])
        i += 1
    return even


def sub(a_list: list[int], start: int, end: int) -> list:
    """Returns a sublist of given list between the specified start index and the end index -1."""
    i: int = 0
    sublist: list[int] = []
    if start < 0: 
        start = 0
    if end > len(a_list):
        end = len(a_list)
    if start > len(a_list) or end <= 0 or len(a_list) == 0:
        return sublist
    else:
        while i < len(a_list):
            if i >= start and i < end:
                sublist.append(a_list[i])
            i += 1 
    return sublist
    

def concat(list1: list[int], list2: list[int]) -> list:
    """Returns all elements of the first and second list together."""
    i: int = 0
    concated: list[int] = []
    while i < len(list1):
        concated.append(list1[i])
        i += 1
    i = 0
    while i < len(list2):
        concated.append(list2[i])
        i += 1
    return concated

        
    