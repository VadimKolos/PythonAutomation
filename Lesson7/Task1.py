def paren_checker(string):
    stack = []
    opening_brackets = "(["
    closing_brackets = ")]"
    bracket_pairs = {")": "(", "]": "["}

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            if stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0
