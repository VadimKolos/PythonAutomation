list_integers = [-2, -3, 0, 1, -1, 2, 4]


def even_numbers_check(lst):
    even_numbers = []
    for i in lst:
        if i % 2 == 0:
            even_numbers.append(i)
            print(i)


even_numbers_check(list_integers)
