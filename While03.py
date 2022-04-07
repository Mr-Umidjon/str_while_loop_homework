def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    import string
    result = string.punctuation

    i = 0
    k = 0

    while i < len(s):
        if s[i] in result:
            k += 1
        i += 1
    return k


print(main("#hashtag@$"))
