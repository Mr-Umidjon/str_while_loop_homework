def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    for i in s:
        if i.isdigit():
            count += 1

    return count


print(main('2j344'))
