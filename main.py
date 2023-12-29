op_arr = ['+', '-', '*', '/', '^', '@', '&', '&', '%']
number_chars_arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


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

def find_closing_parenthesis(expression, opening_index):
    stack = []
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack.pop() == opening_index:
                return i
    return -1  # Indicates no matching closing parenthesis found


# cut the string for 3 parts returning the part inside the between the indexes at index 1
def cut_string_excluding_indices(s, index1, index2):
    part1 = s[:index1]
    part2 = s[index1 + 1:index2]
    part3 = s[index2 + 1:]
    return part1, part2, part3


def create_tree(tree_node):
    string = tree_node.value

    i = 0
    parts = []

    if '(' in string:
        open_index = string.find('(')
        close_index = find_closing_parenthesis(string, open_index)
        first_part, second_part, third_part = cut_string_excluding_indices(string, open_index, close_index)
        second_part_tree = TreeNode(second_part)
        create_tree(second_part_tree)

        second_part = calculate_tree(second_part_tree)
        string = first_part + str(second_part) + third_part

    op_found = False
    while i < len(op_arr) and not op_found:
        if op_arr[i] in string:
            parts = string.split(op_arr[i], 1)
            parts.append(op_arr[i])
            op_found = True
        i += 1


    if (len(parts) == 3):
        tree_node.right = TreeNode(parts[0])
        tree_node.left = TreeNode(parts[1])
        tree_node.value = parts[2]

        create_tree(tree_node.right)
        create_tree(tree_node.left)


def main():
    string = "9*((45+544)+7*8)"
    tree_node = TreeNode(string)
    create_tree(tree_node)
    num = calculate_tree(tree_node)
    print(num)


if __name__ == "__main__":
    main()
