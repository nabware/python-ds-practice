def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    # look at solution

    # keys = set(nums)
    # most_common_key = None
    # highest_count = 0

    # for key in keys:
    #     count = nums.count(key)
    #     if count > highest_count:
    #         highest_count = count
    #         most_common_key = key

    # return most_common_key

    # use max with .items()

    freqs = {}
    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1

    return max(freqs, key=freqs.get)


