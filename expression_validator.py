import main

def are_parentheses_balanced(expression: str) -> bool:
    stack = []

    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0


def is_all_chars_valid(string: str, char_list: list) -> bool:
    for c in string:
        if not (c in char_list):
            return False
    return True


def are_operators_separated(expression: str) -> bool:
    operators = set(main.middle_op_arr)
    previous_char = None

    for char in expression:
        if char in operators and previous_char in operators:
            return False
        previous_char = char

    return True

def validate_expression(string: str, valid_chars: list) -> bool:
    if are_parentheses_balanced(string) and is_all_chars_valid(string, valid_chars) and are_parentheses_balanced(string):
        return True
    else:
        return False
