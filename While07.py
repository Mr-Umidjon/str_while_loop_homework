def main(s):
    """
g    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    k = 0

    while i < len(s):
        son = int(s[i])
        if son % 2 == 0:
            k += 1
        i += 1
    return k


print(main('1234'))
