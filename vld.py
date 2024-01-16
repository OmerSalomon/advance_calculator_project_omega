import main


# return list of all the operators that can not be next to each other
def get_non_adjacent_operator_list() -> list:
    operator_list = main.get_operator_dict().keys()
    # all the operators that can be near each other
    adjacent_operator_list = ['+', '-', '(', ')']
    for char in main.get_un_operator_dict():
        adjacent_operator_list.append(char)

    # all the operators that can not be near each other
    non_adjacent_operator_list = [item for item in operator_list if item not in adjacent_operator_list]

    return non_adjacent_operator_list


# return list of the invalid chars in exp
def get_invalid_chars(exp: str) -> list:
    operator_list = main.get_operator_dict().keys()
    invalid_chars = []
    if ' ' in exp:
        invalid_chars.append(' ')
    for char in exp:
        if not (char.isdigit() or char in operator_list):
            invalid_chars.append(char)
    return invalid_chars


# return true if the parenthesis are balanced
# otherwise return false
def is_parenthesis_balanced(input_string) -> bool:
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
def get_invalid_junction_operators(exp: str) -> list:
    operator_list = main.get_operator_dict().keys()
    non_adjacent_operator = get_non_adjacent_operator_list()
    adjacent_operators_list = []
    for i in range(len(exp) - 1):
        if exp[i] in operator_list and exp[i + 1] in operator_list:
            if exp[i] in non_adjacent_operator and exp[i + 1] in non_adjacent_operator:
                adjacent_operators_list.append(exp[i] + exp[i + 1])

    return adjacent_operators_list


# return list of right un operators that have number right to them
def get_right_un_operator_placement(exp: str) -> list:
    invalid_operators = []

    if exp[0] in main.get_right_un_operator():
        invalid_operators.append(exp[0])

    for i in range(len(exp) - 1):
        if exp[i] in main.get_right_un_operator():
            if exp[i + 1].isdigit():
                invalid_operators.append(exp[i])
        i += 1

    return invalid_operators


# return list of left operators that have digit left to them
def get_left_un_operator_placement(exp: str) -> list:
    invalid_operators = []

    if exp[-1] in main.get_left_un_operator():
        invalid_operators.append(exp[-1])

    i = 1
    while i < len(exp) - 1:
        if exp[i] in main.get_left_un_operator().keys():
            if exp[i - 1].isdigit():
                invalid_operators.append(exp[i])
        i += 1

    return invalid_operators


# return list of all the empty parenthesis
def check_empty_parenthesis(exp: str) -> list:
    empty_parenthesis_list = []
    for i in range(len(exp) - 1):
        if exp[i] == '(' and exp[i + 1] == ')':
            empty_parenthesis_list.append(exp[i])
            empty_parenthesis_list.append(exp[i + 1])

    return empty_parenthesis_list


# make sure there that's not happening (a)b
def get_parenthesis_near_digits(exp: str) -> list:
    parenthesis_near_digits = []
    i = 1
    while i < len(exp) - 1:
        if exp[i] == '(' and exp[i - 1].isdigit():
            parenthesis_near_digits.append(exp[i - 1] + exp[i])
        if exp[i] == ')' and exp[i + 1].isdigit():
            parenthesis_near_digits.append(exp[i] + exp[i + 1])
        i += 1

    return parenthesis_near_digits


def validate_exp(exp: str):
    if len(exp) == 0:
        raise ValueError(f'exp is empty')

    invalid_chars = get_invalid_chars(exp)
    if len(invalid_chars) != 0:
        raise ValueError(f'{invalid_chars} are invalid chars')

    empty_parenthesis = check_empty_parenthesis(exp)
    if len(empty_parenthesis) > 0:
        raise SyntaxError(f'{empty_parenthesis} those parenthesis are empty')

    if not is_parenthesis_balanced(exp):
        raise SyntaxError('parenthesis are not balanced')

    invalid_junction_operators = get_invalid_junction_operators(exp)
    if len(invalid_junction_operators) > 0:
        raise SyntaxError(f'{invalid_junction_operators} those operators can not be next to each other')

    misplaced_left_un_operators = get_left_un_operator_placement(exp)
    if len(misplaced_left_un_operators):
        raise SyntaxError(f'{misplaced_left_un_operators} are misplaced')

    misplaced_right_un_operators = get_right_un_operator_placement(exp)
    if len(misplaced_right_un_operators) > 0:
        raise SyntaxError(f'{misplaced_right_un_operators} are misplaced')

    parenthesis_near_digits = get_parenthesis_near_digits(exp)
    if len(parenthesis_near_digits) > 0:
        raise SyntaxError(f'{parenthesis_near_digits} those parenthesis can not be near those digits')
