import sys

import math_func
import exp_manipulation
import vld


def get_parenthesis_dict() -> dict:
    my_dict = {
        '(': 0,
        ')': 0
    }
    return my_dict


def get_bin_operator_dict() -> dict:
    my_dict = {
        '+': 1,
        '-': 1,
        '/': 2,
        '*': 2,
        '^': 3,
        '%': 4,
        '@': 5,
        '&': 5,
        '$': 5
    }
    return my_dict


def get_un_operator_dict() -> dict:
    my_dict = {}
    my_dict.update(get_right_un_operator())
    my_dict.update(get_left_un_operator())
    return my_dict


def get_right_un_operator() -> dict:
    my_dict = {
        '!': 6,
        '#': 6
    }
    return my_dict


def get_left_un_operator() -> dict:
    my_dict = {
        '~': 6,
        'u': 3.5
    }
    return my_dict


# return dictionary of double operand
# operators as key and their power as values
def get_operator_dict() -> dict[str, int]:
    op_dict = {}
    op_dict.update(get_un_operator_dict())
    op_dict.update(get_bin_operator_dict())
    op_dict.update(get_parenthesis_dict())
    return op_dict


# returning the calculated value of operators that affect two operand
def bin_operand_culc(val_1: float, val_2: float, operator: chr) -> float:
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
        return math_func.perform_pow(val_2, val_1)
    if operator == '@':
        return (val_2 + val_1) / 2
    if operator == '$':
        return max(val_1, val_2)
    if operator == '&':
        return min(val_1, val_2)
    if operator == '%':
        return val_2 % val_1


# returning the calculated value of operators that affect one operand
def un_operand_culc(val: float, operator: chr) -> float:
    val = float(val)
    if operator == '~':
        return -val
    elif operator == '!':
        return math_func.factorial(val)
    elif operator == '#':
        return math_func.perform_digit_addition(val)
    elif operator == 'u':
        return -val


# Calculates the top values in the value
# stack according to the type of the operator
def pop_and_culc(values: list, operators: list):
    result = 0
    max_float = sys.float_info.max
    op = operators.pop()
    if op in get_un_operator_dict().keys():
        val = values.pop()
        result = un_operand_culc(val, op)
        if result > max_float:
            raise ValueError(f'result of {val} {op} is too large to be float')
    else:
        val_1 = values.pop()
        val_2 = values.pop()
        result = bin_operand_culc(val_1, val_2, op)
        if result > max_float:
            raise ValueError(f'result of {val_1} {val_2} {op} is too large to be float')
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


# this function locate every unary minus and replace it with 'u' operator
def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


# return the evaluate value of the expression
def evaluate_exp(exp: str, op_dict: dict) -> float:
    vld.validate_exp(exp)
    exp = exp_manipulation.manipulate_string(exp)
    tokens = split_expression(exp)

    values = []
    operators = []

    for token in tokens:
        if is_number(token):
            values.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                result = pop_and_culc(values, operators)
                values.append(result)
            operators.pop()
            # if token is from the left un type always add it to the operator stack
        elif token in get_left_un_operator().keys():
            operators.append(token)
        elif token in op_dict.keys():
            while len(operators) != 0 and op_dict[operators[-1]] >= op_dict[token]:
                result = pop_and_culc(values, operators)
                values.append(result)
            operators.append(token)

    while len(operators) != 0:
        result = pop_and_culc(values, operators)
        values.append(result)

    evaluated_num = float(values.pop())
    return round(evaluated_num, 3)


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


def test():
    print('Enter expression (type "exit" to quit):')
    exp = input()

    while exp != 'exit':
        result = evaluate_exp(exp, get_operator_dict())
        print(result)

        print('Enter another expression (or "exit" to quit):')
        exp = input()


def main():
    try:
        start()
    except KeyboardInterrupt:
        print("Caught keyboard interrupt. Exiting the program.")
    except EOFError:
        print("EOF error occurred. No input was given.")


if __name__ == "__main__":
    main()
