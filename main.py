import math


def get_single_operand_operators_list():
    single_operand_operators = ['!', '~']
    return single_operand_operators


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
        '(': 0
    }

    return my_dict


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


def factorial(n: float) -> int:
    if n.is_integer() and n < 0:
        raise ValueError("There is no factorial for non native number")
    n = int(n)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def single_operand_culc(val: float, operator: chr) -> float:
    val = float(val)
    if operator == '~':
        return -val
    elif operator == '!':
        return factorial(val)


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


def fix_plus_minus(s: str):
    while ('++' in s) or ('--' in s) or ('-+' in s) or ('+-' in s):
        s = s.replace('++', '+')
        s = s.replace('--', '+')
        s = s.replace('-+', '-')
        s = s.replace('+-', '-')

    return s

def calculate_exp(exp: str, op_dict: dict) -> float:
    exp = fix_plus_minus(exp)
    values = []
    operators = []

    for char in exp:
        if char.isdigit():
            values.append(char)
        elif char == '(':
            operators.append(char)
        elif char in op_dict.keys():
            while len(operators) != 0 and op_dict[operators[-1]] >= op_dict[char]:
                result = pop_and_culc(values, operators)
                values.append(result)
            operators.append(char)
        elif char == ')':
            while operators[-1] != '(':
                result = pop_and_culc(values, operators)
                values.append(result)
            operators.pop()

    while len(operators) != 0:
        result = pop_and_culc(values, operators)
        values.append(result)

    return values.pop()


def main():
    exp = '33'
    result = calculate_exp(exp, get_operator_dict())
    print(result)


if __name__ == "__main__":
    main()
