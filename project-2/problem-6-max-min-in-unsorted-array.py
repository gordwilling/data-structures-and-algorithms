import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = None
    max = None
    if ints:
        min = ints[0]
        max = ints[0]
    for i in range(1, len(ints)):
        if min > ints[i]:
            min = ints[i]
        if max < ints[i]:
            max = ints[i]
    return min, max


if __name__ == '__main__':
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print(get_min_max(l))
    # (0, 9)

    print(get_min_max([]))
    # (None, None)

    print(get_min_max([2, 2, 2, 2, 2]))
    # (2, 2)

    print(get_min_max([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    # (1, 9)
