import re

lexemes = {
        'id': r'[a-zA-Z_][a-zA-Z0-9_]*',
        'int': r'[0-9]+',
        'decimal': r'\.',
        'lparen': r'\(',
        'rparen': r'\)',
        'plus': r'\+',
        'minus': r'\-',
        'times': r'\*',
        'divide': r'/',
        'equals': r'=',
}

tokenize_line = re.compile('|'.join(lexemes.values())).findall

def readlines_as_tokens(file):
    return [tokenize_line(line) for line in file.readlines()]
