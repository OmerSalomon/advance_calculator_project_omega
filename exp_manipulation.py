import main


def fix_plus_minus(s: str) -> str:
    while ('++' in s) or ('--' in s) or ('-+' in s) or ('+-' in s):
        s = s.replace('++', '+')
        s = s.replace('--', '+')
        s = s.replace('-+', '-')
        s = s.replace('+-', '-')

    return s


def replace_unary_minuses_with_u(exp: str) -> str:
    i = 0
    while i < len(exp) - 2:
        if exp[i] == '-':
            right_ne = exp[i + 1]
            left_ne = exp[i - 1]
            if left_ne in main.get_operator_dict() or left_ne == '(' or left_ne == ')':
                if right_ne.isdigit():
                    exp = exp[:i] + 'u' + exp[i + 1:]
        i += 1

    return exp

def manipulate_string(exp: str):
    exp = replace_unary_minuses_with_u(exp)
    exp = fix_plus_minus(exp)
    return exp