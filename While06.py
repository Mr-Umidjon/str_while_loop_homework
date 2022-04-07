def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """

    result = 'aeiou'
    # print(result)

    i = 0
    k = 0

    while i < len(s):
        if s[i] in result:
            k += 1
        i += 1
    return k


print(main('asa'))
