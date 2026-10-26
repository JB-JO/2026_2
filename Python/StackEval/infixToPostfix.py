from StackClass import Stack
from Precedence import *

def infix_to_postfix(expr):
    s = Stack(100)
    output = []

    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.is_empty():
                op = s.pop()
                if op=='(':
                    break;
                else:
                    output.append(op)

        elif term in "+-*/":
            while not s.is_empty() and s.peek() != '(':
                op = s.peek()
                if (precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)

        else:
            output.append(term)

    while not s.is_empty():
        output.append(s.pop())

    return output