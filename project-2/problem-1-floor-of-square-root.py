from math import floor, ceil


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    def midpoint(min, max):
        return min + (max - min) / 2

    def loop(n, min, max):
        candidate = midpoint(min, max)
        squared = candidate ** 2
        floor_squared = floor(candidate) ** 2
        ceil_squared = ceil(candidate) ** 2

        if ceil_squared == n:
            return ceil(candidate)

        if floor_squared <= n < ceil_squared:
            return floor(candidate)

        if floor_squared == n:
            return floor(candidate)

        if squared > n:
            return loop(n, min, midpoint(min, max))
        else:
            return loop(n, midpoint(min, max), max)

    if number < 0:
        return None
    if number == 0:
        return 0
    if number == 1:
        return 1

    return loop(number, 0, number)


if __name__ == '__main__':

    print(sqrt(-1))
    # None
    print(sqrt(0))
    # 0
    print(sqrt(1))
    # 1
    print(sqrt(2))
    # 1
    print(sqrt(3))
    # 1
    print(sqrt(4))
    # 2
    print(sqrt(5))
    # 2
    print(sqrt(6))
    # 2
    print(sqrt(7))
    # 2
    print(sqrt(8))
    # 2
    print(sqrt(9))
    # 3
    print(sqrt(10))
    # 3
    print(sqrt(16))
    # 4
    print(sqrt(25))
    # 5
    print(sqrt(36))
    # 6
    print(sqrt(49))
    # 7
    print(sqrt(64))
    # 8
    print(sqrt(81))
    # 9
    print(sqrt(100))
    # 10
    print(sqrt(121))
    # 11
    print(sqrt(132))
    # 11
    print(sqrt(144))
    # 12
