import random

def quiz():
    score = 0

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 5)
    num4 = random.randint(1, 3)

    answer1 = int(input(f"Question 1: What is {num1} + {num2}? "))
    if answer1 == num1 + num2:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

    answer2 = int(input(f"Question 2: What is {num1} * {num2}? "))
    if answer2 == num1 * num2:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

    answer3 = int(input(f"Question 3: What is {num3} to the power of {num4}? "))
    if answer3 == num3 ** num4:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

    print(f"Total score: {score}.")

quiz()