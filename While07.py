def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    k = 0

    while i < len(s):
        son = int(i)
        if son % 2 == 0:
            k += 1
        i += 1
    return k


print(main('1234'))
