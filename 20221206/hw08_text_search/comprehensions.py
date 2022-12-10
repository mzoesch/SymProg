# This exercise contains 5 Tasks to practice comprehensions.
# With these, multiple-line for-loop constructions can be expressed in expressive one-liners.


def multiply_by(x, list1):
    """
    Multiplies each value in list1 by x and returns it as a new list.
    """

    # return None  # TODO: replace

    return [
        x * i
        for i in list1
    ]


def check_division(x, list1):
    """
    Takes a list and returns a list indicating whether or not each element in the original list can be exactly divided (without remainder) by x.
    (e.g check\_division(3, [1,2,3]) -> [False, False, True])
    """

    # return None  # TODO: replace

    return [
        i % x == 0
        for i in list1
    ]


def div_less(set1):
    """
    Return a new set only containing numbers that can`t be divided by any other number (except itself and 1)
    from the original set.
    """

    # return None  # TODO: replace

    return {
        i
        for i in set1
        if all(
            i % j != 0
            for j in set1
            if j != i and j != 1
        )
    }


def map_zip(list1, list2):
    """
    It should return a dictionary mapping the 'nth' element in list1 to the 'nth' element in list2.
    Make use of the 'zip()' function in your dictionary comprehension, that can handle lists of different sizes
    automatically.
    """

    # return None  # TODO: replace

    return {
        i: j
        for i, j in zip(list1, list2)
    }


def word_to_length(list1):
    """
    Returns a dictionary mapping all words with at least 3 characters to their number of characters.
    """

    # return None  # TODO: replace

    return {
        i: len(i)
        for i in list1
        if len(i) >= 3
    }
