def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k = 0
    son = int(s)

    while son > 0:
        son1 = son % 10
        son //= 10
        k += son1

    return k


print(main('12345'))
