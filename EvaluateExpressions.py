from Stack import Stack

# Evaluates an arithmetic expression
def evaluate_expression(expression):
    operandStack = Stack()
    operatorStack = Stack()
    expression = insert_blanks(expression)
    tokens = expression.split(" ")

    for token in tokens:
        token = token.strip()
        if token == '':
            continue
        if token == '+' or token == '-':
            while (not operatorStack.isEmpty() and
                   operatorStack.peek() == '+'
                or operatorStack.peek() == '-'
                or operatorStack.peek() == '*'
                or operatorStack.peek() == '/'):
                processandoperator(operandStack, operatorStack)
            operatorStack.push(token)
        elif token == '*' or token == '/':
            while (not operatorStack.isEmpty() and
                   operatorStack.peek() == '*'
                or operatorStack.peek() == '/'):
                processandoperator(operandStack, operatorStack)
            operatorStack.push(token)
        elif token == '(':
            operatorStack.push('(')
        elif token == ')':
            while operatorStack.peek() != '(':
                processandoperator(operandStack, operatorStack)
            operatorStack.pop() # pop the '(' symbol
        else:
            operandStack.push(int(token))

    while not operatorStack.isEmpty():
        processandoperator(operandStack, operatorStack)

    return operandStack.pop()


# Process one operator
def processandoperator(operandstack, operatorstack):
    # Get the operator
    op = operatorstack.pop()

    # Get the two operands
    op1 = operandstack.pop()
    op2 = operandstack.pop()

    # Do the artithmetic evaluation
    if op == '+':
        operandstack.push(op2 + op1)
    elif op == '-':
        operandstack.push(op2 - op1)
    elif op == '*':
        operandstack.push(op2 * op1)
    elif op == '/':
        operandstack.push(op2 / op1)

# This function adds spaces around operands so that we can tokenize the expression
# For instance, an expression like '(2+3)*5-3' will be converted to ' ( 2 + 3 ) * 5 - 3'
def insert_blanks(s):
    result = ''
    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == ')' or s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
            result += ' ' + s [i] + ' '
        else:
            result += s[i]

    return result

def main():
    expression = input('Type in the expression')
    result = evaluate_expression(expression)
    print(expression, '=', result)

main()

