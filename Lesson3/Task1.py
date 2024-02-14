try:
    a, b = float(input("input number: ")), float(input("input second number: "))

    if a * b >= 0:
        print("result: ", ((a * b) ** 0.5))
    else:
        print("Impossible to calculate the square root of a negative number")
except ValueError:
    print("Incorrect input")