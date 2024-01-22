import main


# Simplifies the expression by resolving redundant plus and minus signs.
# This function iteratively replaces instances of '++', '--', '-+', and '+-'
# with their simplified equivalents. '++' and '--' become '+', while
# '-+' and '+-' become '-'.
#
# Args:
# s (str): A string representing a mathematical expression.
#
# Returns:
# str: The simplified expression with redundant signs resolved.

# Replaces unary minus operators in the expression with 'u'.
# This function scans the expression and replaces each unary minus (a minus sign
# that operates on a single operand) with the character 'u'. This is useful for
# differentiating unary and binary minus signs in parsing or evaluating the expression.
#
# Args:
# exp (str): A string representing a mathematical expression.
#
# Returns:
# str: The expression with unary minus operators replaced by 'u'.
def replace_unary_minuses_with_u(exp: str) -> str:
    if len(exp) <= 1:
        return exp

    # Replace the initial minus if it's unary
    if exp[0] == '-':
        if exp[1].isdigit() or exp[1] in main.get_parenthesis_dict() or exp[1] == '-':
            exp = exp[:0] + 'u' + exp[0 + 1:]  # replace the first char of exp with 'u'

    i = 0
    while i < len(exp) - 1:
        if exp[i] == '-':
            right_ne = exp[i + 1]
            left_ne = exp[i - 1]
            # Check the context of the minus sign to determine if it's unary
            if left_ne in main.get_operator_dict().keys() or left_ne in main.get_parenthesis_dict():
                if right_ne.isdigit() or right_ne == '-' or left_ne in main.get_parenthesis_dict():
                    exp = exp[:i] + 'u' + exp[i + 1:]
        i += 1

    return exp


def manipulate_string(exp: str):
    exp = replace_unary_minuses_with_u(exp)
    return exp
