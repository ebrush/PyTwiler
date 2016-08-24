import re
import tokenizer

add = lambda a, b: a + b
sub = lambda a, b: a - b
mult = lambda a, b: a * b
div = lambda a, b: a / b

#decorator for debugging
def log_result(f):
    def logged_func(*args, **kwargs):
        res = f(*args, **kwargs)
        print('debug:', res)
        return res
    return logged_func

#@log_result
def e(t):
    if type(t) == list and len(t) == 1:
        return t[0]
    elif type(t) is str and re.match(tokenizer.lexemes['id'], t):
        return globals()[t]
    elif type(t) is not list:
        return t

    if t[1] == '+':
        op = add
    elif t[1] == '-':
        op = sub
    elif t[1] == '*':
        op = mult
    elif t[1] == '/':
        op = div
    elif t[1] == '=':
        assign_var = t[0]
        globals()[assign_var] = e(t[2:])
        return globals()[assign_var]
    else:
        raise SyntaxError('Unexpected symbol during parsing: ' + t[1])
    
    if op is add:
        return op(e(t[0]), e(t[2:]))
    
    elif op is mult or op is div:
        return e([op(e(t[0]), e(t[2]))] + t[3:])

    elif op is sub:
        t[1] = '+'
        t[2] *= -1
        return e(t)
