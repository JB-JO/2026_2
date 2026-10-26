def precedence(op):
    if op == '(' or op == ')' : return 0
    elif op == '+' or op == '-': return 1
    elif op == '*' or op == '/': return 2
    else: return -1

