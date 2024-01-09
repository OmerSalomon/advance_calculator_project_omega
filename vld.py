# return list of the invalid chars in exp
def get_invalid_chars(exp: str, operator_list: set) -> list:
    invalid_chars = []
    for char in exp:
        if not (char.isdigit() or char in operator_list or ')'):
            invalid_chars.append(char)
    return invalid_chars


# return true if the parenthesis are balanced
# otherwise return false
def is_parenthesis_balanced(input_string):
    balance = 0

    for char in input_string:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False

    return balance == 0


# returns list of invalid adjacent operators
def get_misplaced_operators(input_string: str, char_list: list) -> list:
    adjacent_operators_list = []
    for i in range(len(input_string) - 1):
        if input_string[i] in char_list and input_string[i] == input_string[i + 1]:
            adjacent_operators_list.append(input_string[i] + input_string[i + 1])
    return adjacent_operators_list
