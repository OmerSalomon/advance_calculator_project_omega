def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1


def associativity(c):
    if c == '^':
        return 'R'
    return 'L'  # Default to left-associative


def infix_to_postfix(s):
    result = []
    stack = []

    for i in range(len(s)):
        c = s[i]

        # If the scanned character is an operand, add it to the output string.
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            result.append(c)
        # If the scanned character is an ‘(‘, push it to the stack.
        elif c == '(':
            stack.append(c)
        # If the scanned character is an ‘)’, pop and add to the output string from the stack
        # until an ‘(‘ is encountered.
        elif c == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Pop '('
        # If an operator is scanned
        else:
            while stack and (prec(s[i]) < prec(stack[-1]) or
                             (prec(s[i]) == prec(stack[-1]) and associativity(s[i]) == 'L')):
                result.append(stack.pop())
            stack.append(c)

    # Pop all the remaining elements from the stack
    while stack:
        result.append(stack.pop())

    print(''.join(result))


# Python program to evaluate value of a postfix expression


# Class to convert the expression
class Evaluate:

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity

        # This array is used a stack
        self.array = []

    # Check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)

    # The main function that converts given infix expression
    # to postfix expression
    def evaluatePostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:

            # If the scanned character is an operand
            # (number here) push it to the stack
            if i.isdigit():
                self.push(i)

            # If the scanned character is an operator,
            # pop two elements from stack and apply it.
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))

        return int(self.pop())


# Driver code
if __name__ == '__main__':
    exp = "231*+9-"
    obj = Evaluate(len(exp))

    # Function call
    print("postfix evaluation: %d" % (obj.evaluatePostfix(exp)))


# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


def main():
    # Driver code
    exp = "a+b*(c^d-e)^(f+g*h)-i"

    # Function call
    infix_to_postfix(exp)


if __name__ == "__main__":
    main()
