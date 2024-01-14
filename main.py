import math
import json
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
        'u': 3.5,
        '%': 4,
        '@': 5,
        '&': 5,
    }
    return my_dict


def get_un_operator_dict():
    my_dict = {
        'u': 3.5,
        '!': 6,
        '~': 6,
        '#': 6
    }
    return my_dict


# return dictionary of double operand operators as key and their power as values
def get_operator_dict() -> dict[str, int]:
    op_dict = {}
    op_dict.update(get_un_operator_dict())
    op_dict.update(get_bin_operator_dict())
    op_dict.update(get_parenthesis_dict())
    return op_dict


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
    if operator == '%':
        return val_2 % val_1


# returning the calculated value of operators that affect one operand
def single_operand_culc(val: float, operator: chr) -> float:
    val = float(val)
    if operator == '~':
        return -val
    elif operator == '!':
        return factorial(val)
    elif operator == '#':
        val = str(val)
        val = val.replace('.', '')
        res = 0
        for digit in val:
            res += int(digit)
        return res
    elif operator == 'u':
        return -val


# Calculates the top values in the value stack according to the type of the operator
def pop_and_culc(values: list, operators: list):
    op = operators.pop()
    if op in get_un_operator_dict().keys():
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


def replace_unary_minuses_with_u(exp: str) -> str:
    if len(exp) <= 1:
        return exp

    if exp[0] == '-' and (is_number(exp[1]) or exp[1] == '(' or exp[1] == ')'):
        exp[0] = 'u'

    i = 0
    while i < len(exp) - 1:
        if exp[i] == '-':
            right_ne = exp[i + 1]
            left_ne = exp[i - 1]
            if left_ne in get_operator_dict() or left_ne == '(' or left_ne == ')':
                if right_ne.isdigit():
                    exp = exp[:i] + 'u' + exp[i + 1:]
        i += 1

    return exp


# this function locate every unary minus and replace it with 'u' operator


def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


# return the evaluate value of the expression
def evaluate_exp(exp: str, op_dict: dict) -> float:
    values = []
    operators = []

    exp = replace_unary_minuses_with_u(exp)
    exp = fix_plus_minus(exp)

    invalid_chars = vld.get_invalid_chars(exp, get_operator_dict().keys())
    if (len(invalid_chars) != 0):
        raise ValueError(f'{invalid_chars} are invalid chars')

    if not vld.is_parenthesis_balanced(exp):
        raise ValueError('parenthesis are not balanced')

    misplaced_operators = vld.get_misplaced_operators(exp)
    if len(misplaced_operators) > 0:
        raise ValueError(f'{misplaced_operators} those operators can not be next to each other')

    tokens = split_expression(exp)

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


def add(num1, num2):
    return num1 + num2


def fun(val1, val2):
    return val1 + val2


def main():
    start()


if __name__ == "__main__":
    main()
