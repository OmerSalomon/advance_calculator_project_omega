import math


# return list of all the operators that can not be next to each other
def get_non_adjacent_operator_list():
    operator_list = list(get_operator_dict().keys()).copy()
    adjacent_operator_list = ['+', '-', '(', ')']
    non_adjacent_operator_list = [item for item in operator_list if item not in adjacent_operator_list]

    return non_adjacent_operator_list


# return dictionary of single operand operators as key and their power as values
def get_single_operand_operators_list():
    single_operand_operators = ['!', '~']
    return single_operand_operators


# return dictionary of double operand operators as key and their power as values
def get_operator_dict():
    my_dict = {
        '+': 1,
        '-': 1,
        '/': 2,
        '*': 2,
        '^': 3,
        '@': 5,
        '&': 5,
        '!': 6,
        '~': 6,
        '(': 0,
        ')': 0
    }

    return my_dict


# returning n!
def factorial(n: float) -> int:
    if n.is_integer() and n < 0:
        raise ValueError("There is no factorial for non native number")
    n = int(n)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# returning the calculated value of operators that affect two operand
def double_operand_culc(val_1: float, val_2: float, operator: chr) -> float:
    val_1 = float(val_1)
    val_2 = float(val_2)

    if operator == '+':
        return val_2 + val_1
    if operator == '-':
        return val_2 - val_1
    if operator == '/':
        return val_2 / val_1
    if operator == '*':
        return val_2 * val_1
    if operator == '^':
        return math.pow(val_2, val_1)
    if operator == '@':
        return (val_2 + val_1) / 2
    if operator == '$':
        if val_2 > val_1:
            return val_2
        else:
            return val_1
    if operator == '&':
        if val_2 < val_1:
            return val_2
        else:
            return val_1


# returning the calculated value of operators that affect one operand
def single_operand_culc(val: float, operator: chr) -> float:
    val = float(val)
    if operator == '~':
        return -val
    elif operator == '!':
        return factorial(val)


# Calculates the top values in the value stack according to the type of the operator
def pop_and_culc(values: list, operators: list):
    op = operators.pop()
    if op in get_single_operand_operators_list():
        val = values.pop()
        result = single_operand_culc(val, op)
        return result
    else:
        val_1 = values.pop()
        val_2 = values.pop()
        result = double_operand_culc(val_1, val_2, op)
        return result


def split_expression(expression):
    result = []
    number = ''

    for char in expression:
        if char.isdigit() or char == '.':
            number += char
        else:
            if number:
                result.append(number)
                number = ''
            if char in get_operator_dict().keys():
                result.append(char)
    if number:
        result.append(number)

    return result


# Reducing minuses and pluses
# Returning reduced string
def fix_plus_minus(s: str) -> str:
    while ('++' in s) or ('--' in s) or ('-+' in s) or ('+-' in s):
        s = s.replace('++', '+')
        s = s.replace('--', '+')
        s = s.replace('-+', '-')
        s = s.replace('+-', '-')

    return s


def check_for_invalid_char(exp: str, operator_list: set) -> list:
    invalid_chars = []
    for char in exp:
        if not (char.isdigit() or char in operator_list or ')'):
            invalid_chars.append(char)
    return invalid_chars


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
def are_chars_non_adjacent(input_string: str, char_list: list[chr]) -> list:
    adjacent_operators_list = []
    for i in range(len(input_string) - 1):
        if input_string[i] in char_list and input_string[i] == input_string[i + 1]:
            adjacent_operators_list.append(input_string[i] + input_string[i + 1])
    return adjacent_operators_list


def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


# return the evaluate value of the expression
def evaluate_exp(exp: str, op_dict: dict) -> float:
    exp = fix_plus_minus(exp)
    values = []
    operators = []

    invalid_chars = check_for_invalid_char(exp, get_operator_dict().keys())
    if (len(invalid_chars) != 0):
        raise ValueError(f'{invalid_chars} are invalid chars')

    if not is_parenthesis_balanced(exp):
        raise ValueError('parenthesis are not balanced')

    adjacent_operators_list = are_chars_non_adjacent(exp, get_non_adjacent_operator_list())
    if len(adjacent_operators_list) > 0:
        raise ValueError(f'{adjacent_operators_list} those operators can not be next to each other')

    exp_tokens = split_expression(exp)

    for token in exp_tokens:
        if is_number(token):
            values.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                result = pop_and_culc(values, operators)
                values.append(result)
            operators.pop()
        elif token in op_dict.keys():
            while len(operators) != 0 and op_dict[operators[-1]] >= op_dict[token]:
                result = pop_and_culc(values, operators)
                values.append(result)
            operators.append(token)

    while len(operators) != 0:
        result = pop_and_culc(values, operators)
        values.append(result)

    return values.pop()


def start():
    print('Enter expression (type "exit" to quit):')
    exp = input()

    while exp != 'exit':
        try:
            result = evaluate_exp(exp, get_operator_dict())
            print(result)
        except ValueError as e:
            print(f"Value Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        print('Enter another expression (or "exit" to quit):')
        exp = input()


def main():
    start()


if __name__ == "__main__":
    main()
