user_input = input("Input string: ")

if not user_input.isalpha() or user_input.strip() == '':
    print("Incorrect input.")
else:
    input_str = user_input.lower()

    if input_str == input_str[::-1]:
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")