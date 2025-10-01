def is_even(n: int):
    """
    returns True if the provided value is even, else False
    """

    return n % 2 == 0


def number_of_even_values_in_list(l: list):
    """
    returns the number of even numbers in a list
    """
    n_e = sum([1 if is_even(item) else 0 for item in l])
    return n_e


def any_even_in_list(l: list):
    """
    returns True is there is at least an even value in a list, False otherwise.
    """
    for num in l:
        if is_even(num):
            return True

    return False


def largest_in_list(l: list):
    """
    returns the largest value in a list
    """
    if len(l):
        max_num = l[0]
        for num in l[1:]:
            if num > max_num:
                max_num = num
        return max_num
    else:
        return "no entries in the list"


def odd_values_in_list(l: list):
    """
    returns all the odd values in a given list l
    """
    odds = []
    for val in l:
        if isinstance(val, int) and not is_even(val):
            odds.append(val)
    return odds


print(is_even(45.5))
print(number_of_even_values_in_list([1, 2, 3.5, 55, 6, 96]))
print(any_even_in_list([1, 2, 3, 5, 7, 9, 3, 4]))
print(largest_in_list([1, 5, 8, 34, 3, 9, 11]))
print(odd_values_in_list([1, 3, 4, 5, 6, 8, 9]))
