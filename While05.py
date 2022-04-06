def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    k = 0

    while i < len(s):
        if s[i].islower():
            k += 1
        i += 1
    return k


print(main('ag12a'))
