def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    k = 0

    while i < len(s):
        son = int(s[i])
        if son % 2 == 1:
            k += son
        i += 1
    return k


print(main('1234'))
