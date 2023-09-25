def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    # letter_sum = 0

    # for char in word:
    #     if char.lower() == letter.lower(): letter_sum += 1

    # return letter_sum

    return sum([1 for c in word if c.lower() == letter.lower()])
