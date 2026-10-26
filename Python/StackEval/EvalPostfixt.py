from StackClass import Stack
from Precedence import*
from infixToPostfix import*


def eval_postfix(expr):
    s = Stack(100)

    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if (token == '+'): s.push(val1 + val2)
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else:
            s.push(float(token))

    return s.pop()

expression = input("입력 수식(공백문자로 분리) = ")
infix = expression.split()
print("중위표기: ", infix)

postfix = infix_to_postfix(infix)
print("후위표기 : ", postfix)

result = eval_postfix(postfix)
print("계산결과: ", result)
