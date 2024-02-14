list_integers = [-2, -3, 0, 1, -1, 2, 4]


def even_numbers_check(x):
    return x % 2 == 0


print(list(filter(even_numbers_check, list_integers)))
