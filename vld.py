# return list of all the operators that can not be next to each other
from main import get_operator_dict


def get_non_adjacent_operator_list():
    operator_list = list(get_operator_dict().keys()).copy()
    # all the operators that can be near each other
    adjacent_operator_list = ['+', '-', '(', ')', '!']

    # all the operators that can not be near each other
    non_adjacent_operator_list = [item for item in operator_list if item not in adjacent_operator_list]

    return non_adjacent_operator_list


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
def get_misplaced_operators(exp: str) -> list:
    non_adjacent_operator = get_non_adjacent_operator_list()
    operator_list = get_operator_dict().keys()
    adjacent_operators_list = []
    for i in range(len(exp) - 2):
        if exp[i] in operator_list and exp[i+1] in operator_list:
            if exp[i] in non_adjacent_operator or exp[i+1] in non_adjacent_operator:
                adjacent_operators_list.append(exp[i] + exp[i + 1])

    return adjacent_operators_list
