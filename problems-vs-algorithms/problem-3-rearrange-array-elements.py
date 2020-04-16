def quick_sort(input_list):
    def partition(left_index, pivot_index):
        pivot_value = input_list[pivot_index]
        while pivot_index != left_index:
            value = input_list[left_index]

            if value > pivot_value:
                input_list[left_index] = input_list[pivot_index - 1]
                input_list[pivot_index - 1] = pivot_value
                input_list[pivot_index] = value
                pivot_index -= 1
            else:
                left_index += 1

        return pivot_index

    def partition_all(left_index, right_index):
        if left_index < right_index:
            pivot_index = partition(left_index, right_index)
            partition_all(left_index, pivot_index - 1)
            partition_all(pivot_index + 1, right_index)

    partition_all(0, len(input_list) - 1)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    quick_sort(input_list)

    x = 0
    y = 0
    power = 0
    for index in range(0, len(input_list), 2):
        x += input_list[index] * (10 ** power)
        if index < len(input_list) - 1:
            y += input_list[index + 1] * (10 ** power)
        power += 1

    return [x, y]


if __name__ == '__main__':
    print(rearrange_digits([]))
    # [0, 0]

    print(rearrange_digits([1, 2, 3, 4, 5]))
    # [531, 42]

    print(rearrange_digits([4, 6, 2, 5, 9, 8]))
    # [852, 964]

    print(rearrange_digits([4, 6, 2, 5, -9, 8]))
    # [631, 852]

    print(rearrange_digits([-4, -6, -2, -5, -9, -8]))
    # [-469, -258]
