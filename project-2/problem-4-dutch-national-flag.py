def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    i = 0
    next_0 = 0
    next_2 = len(input_list) - 1

    while i <= next_2:
        if input_list[i] == 0:
            input_list[i] = input_list[next_0]
            input_list[next_0] = 0
            next_0 += 1
            i += 1
        elif input_list[i] == 2:
            input_list[i] = input_list[next_2]
            input_list[next_2] = 2
            next_2 -= 1
        else:
            i += 1

    return input_list


if __name__ == '__main__':
    print(sort_012([]))
    # []

    print(sort_012([2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0]))
    # [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]

    print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
    # [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

    print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

    print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
    # [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

    print(sort_012([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
