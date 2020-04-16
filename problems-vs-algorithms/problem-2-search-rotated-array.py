def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    def midpoint(min_index, max_index):
        return min_index + (max_index - min_index) // 2

    def binary_search(min_index, max_index):
        mid_index = midpoint(min_index, max_index)

        if number == input_list[mid_index]:
            return mid_index
        if number == input_list[max_index]:
            return max_index

        if min_index == mid_index:
            # search was exhausted; not found
            return -1

        if number < input_list[mid_index]:
            return binary_search(min_index, mid_index)
        if number > input_list[mid_index]:
            return binary_search(mid_index, max_index)

    def find_start(left_index, right_index):
        if left_index + 1 == right_index:
            # the indices are adjacent
            if input_list[left_index] > input_list[right_index]:
                # and the value at the lower index is larger; the start is at the index on the right
                return right_index

        left_value = input_list[left_index]
        right_value = input_list[right_index]

        if left_value < right_value:
            # this section is sorted;
            if left_index == 0 and right_index == len(input_list) - 1:
                # the whole list is already sorted
                return 0

            # the start lies in the other half
            return find_start(right_index, len(input_list) - 1)

        if left_value > right_value:
            # this section is not sorted; start is within this half
            return find_start(left_index, midpoint(left_index, right_index))

    if not input_list:
        return -1

    max_index = len(input_list) - 1
    start_index = find_start(0, max_index)
    if input_list[start_index] == number:
        return start_index

    end_index = max_index if start_index == 0 else start_index - 1
    if input_list[0] <= number <= input_list[end_index]:
        return binary_search(0, end_index)
    else:
        return binary_search(start_index, max_index)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    # number is at the beginning of the input list
    print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
    # 0

    # number is at the end of the input list
    print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 4))
    # 6

    # number is at the start of the sort order
    print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
    # 5

    # number is at the end of the sort order
    print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8))
    # 2

    # number is before the start of the sort order
    print(rotated_array_search([6, 7, 8, 9, 2, 3, 4], 8))
    # 2

    # number is after the start of the sort order
    print(rotated_array_search([6, 7, 8, 9, 10, 3, 4, 5], 5))
    # 6

    # number is not in the list
    print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10))
    # -1

    # the input list is in sorted order
    print(rotated_array_search([6, 7, 8, 9, 10, 11, 12], 12))
    # 6

    # the input list is empty
    print(rotated_array_search([], 1))
    # -1


