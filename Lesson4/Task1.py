def multiply_numbers(*numbers):
    result = 1
    for i in numbers:
        result = result * i
    print("result: ", result)


multiply_numbers(1, 4, 2, 3)
