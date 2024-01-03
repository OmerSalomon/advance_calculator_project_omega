import math


def get_operator_dict():
    my_dict = {
        '+': 1,
        '-': 1,
        '/': 2,
        '*': 2,
        '^': 3,
        '@': 5,
        '&': 5,
        '(': 0
    }

    return my_dict

def culc(val_1: float, val_2: float, operator: chr) -> float:
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


def pop_and_culc(values: list, operators: list):
    op = operators.pop()
    val_1 = values.pop()
    val_2 = values.pop()
    result = culc(val_1, val_2, op)
    return result


def calculate_exp(exp: str, op_dict: dict):
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
    exp = '9/3^2'
    result = calculate_exp(exp, get_operator_dict())
    print(result)


if __name__ == "__main__":
    main()
