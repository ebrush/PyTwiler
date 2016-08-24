
def listify_parens(tokens, i):
    cur = i
    while tokens[cur] != ')':
        cur += 1
        if tokens[cur] == '(':
            listify_parens(tokens, cur)
    tokens[i] = tokens[i + 1 : cur]
    while cur != i:
        tokens.pop(cur)
        cur -= 1
