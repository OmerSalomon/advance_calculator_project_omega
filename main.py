import test

op_arr = ['+', '-', '*', '/']
number_chars_arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
parentheses_arr = ['(', ')']

def split_expression_test(expr):
    balance = 0
    for i in range(len(expr)):
        if expr[i] == '(':
            balance += 1
        elif expr[i] == ')':
            balance -= 1

        # Check if the parentheses are balanced and we are at or past the halfway point
        if balance == 0 and i >= len(expr) // 2:
            return expr[:i + 1], expr[i + 1:]

    return expr, ''  # Return the whole string and an empty string if no split point is found

# Example usage



def main():
    test.main()

def split_expression(expr):
    parts = []

    # Loop over each character in the expression
    for char in expr:
        if char.isalpha():  # If the character is a letter, it's a variable
            parts.append(char)
        elif char in ['*', '/', '+', '-']:  # If it's an operator
            parts.append(char)
        elif char == '(':  # If it's an opening parenthesis
            start = expr.index(char)  # Find the start index
            end = expr.rindex(')')  # Find the closing parenthesis
            parts.append(expr[start:end + 1])  # Add the whole parenthesis part
            break  # Break the loop as the rest of the string is already processed

    return parts


def find_closing_parenthesis(expression, opening_index) -> int:
    stack = []

    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack and stack[-1] == opening_index:
                return i  # Found the matching closing parenthesis
            stack.pop()

    return -1

def remove_char_at_index(s, i):
    return s[:i] + s[i + 1:]


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def calculate_tree(node):
    if node.left is None and node.right is None:
        return int(node.value)  # Assuming the node is an operand (number)

    left_val = calculate_tree(node.left)
    right_val = calculate_tree(node.right)

    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val


def split_string_by_two_indices_and_remove_empty(s, index1, index2):
    index2 += 1

    parts = (
        s[:index1],   # From start to index1
        s[index1:index2],  # From index1 to index2
        s[index2:]    # From index2 to end
    )

    # Filter out any empty strings
    return tuple(part for part in parts if part)

def slice_for_parenthesis(string):
    open_parenthesis_index = string.find('(')
    close_parenthesis_index = find_closing_parenthesis(string, open_parenthesis_index)
    string_1, string_2 = split_string_by_two_indices_and_remove_empty(string, open_parenthesis_index, close_parenthesis_index)

    parentheses_string = ""
    none_parentheses_string = ""

    first_char_is_operand = False
    op = ''

    if string_1[0] == '(':
        parentheses_string = string_1
        none_parentheses_string = string_2
        first_char_is_operand = True
    else:
        parentheses_string = string_1
        none_parentheses_string = string_1

    parentheses_string = parentheses_string[1:-1]

    if first_char_is_operand:
        op = none_parentheses_string[0]
        none_parentheses_string = none_parentheses_string[1:]
    else:
        op = none_parentheses_string[len(none_parentheses_string) - 1]
        none_parentheses_string = none_parentheses_string[:-1]

    return [none_parentheses_string, parentheses_string, op]

def is_all_char_valid(string: str) -> bool:
    valid_chars = op_arr + number_chars_arr + parentheses_arr

    for char_to_check in string:
        if not char_to_check in string:
            return False

    return True


def is_all_parenthesis_right(string) -> bool:
    parenthesis_stack = []

    for char in string:
        if char == '(':
            parenthesis_stack.append('(')
        elif char == ')':
            if len(parenthesis_stack) != 0:
                if parenthesis_stack[-1] == '(':
                    parenthesis_stack.pop()
                else:
                    return False
            else:
                return False

    if len(parenthesis_stack) == 0:
        return True

    return False


def calculate_expression(string) -> int:
    if not is_all_char_valid(string):
        raise ValueError("not all the chars are valid")

    if not is_all_parenthesis_right(string):
        raise ValueError("parenthesis are not valid")

    treeNode = TreeNode(string)
    create_tree(treeNode)


def create_tree(tree_node: TreeNode):
    string = tree_node.value

    parts = []
    i = 0

    if '(' in string:
        parts = slice_for_parenthesis(string)
    else:
        while i < len(op_arr):
            if op_arr[i] in string:
                parts = string.split(op_arr[i], 1)
                parts.append(op_arr[i])
            i += 1

    if (len(parts) == 3):
        tree_node.right = TreeNode(parts[0])
        tree_node.left = TreeNode(parts[1])
        tree_node.value = parts[2]

        create_tree(tree_node.right)
        create_tree(tree_node.left)


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * 4 * level + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            if node.left:
                print_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * 4 * (level + 1) + "L--- None")

            if node.right:
                print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * 4 * (level + 1) + "R--- None")


if __name__ == "__main__":
    main()
