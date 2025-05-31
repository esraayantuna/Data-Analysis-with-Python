from Stack import Stack

def inspect_parentheses(expression):
    parenthesesStack = Stack()
    expression = insert_blanks(expression)
    tokens = expression.split(" ")

    for token in tokens:
        token = token.strip()
        if token == '':
            continue

        # Peek the top element.  If it is the same as the current
        # element we're trying to push, then just pop it.
        # For instance, if stack now has "[(" and the next token is ")",
        # then we should just pop "(" and continue.
        topElement = parenthesesStack.peek()
        if topElement is not None \
                and (token == ')' and topElement == '('\
                or token == '}' and topElement == '{' \
                or token == ']' and topElement == '['):
            parenthesesStack.pop()
        else:
            parenthesesStack.push(token)

    if parenthesesStack.getSize() == 0:
        return True
    else:
        return False

# This function adds spaces around operands so that we can tokenize the expression
# For instance, an expression like '([])' will be converted to ' ( [ ] ) '
def insert_blanks(s):
    result = ''
    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == ')' \
                or s[i] == '[' or s[i] == ']' \
                or s[i] == '{' or s[i] == '}':
            result += ' ' + s [i] + ' '
        else:
            result += s[i]

    return result


def main():
    expression = '[()]{}{[()()]()}'
    result = inspect_parentheses(expression)
    print(expression, '->', result)

    expression = '[(])'
    result = inspect_parentheses(expression)
    print(expression, '->', result)

main()

