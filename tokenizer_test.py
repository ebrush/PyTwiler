import io
import tokenizer

def test_blank_file():
    blank_file = io.StringIO('')
    assert tokenizer.readlines_as_tokens(blank_file) == []

def test_blank_line_file():
    blank_line_file = io.StringIO('\n')
    assert tokenizer.readlines_as_tokens(blank_line_file) == [[]]

def test_basic_expression_in_line():
    file = io.StringIO('5 + 6*4')
    assert tokenizer.readlines_as_tokens(file) == [['5', '+', '6', '*', '4']]

def test_complex_assignment_in_line():
    file = io.StringIO('a = b = cathead = d = dog + 4 * (72 - (23+26) / animals * 3) / (4 + 3) * catdog27')
    assert tokenizer.readlines_as_tokens(file) == [['a', '=', 'b', '=', 'cathead', '=', 'd', '=', 'dog', '+', '4', '*', '(', '72', '-', '(','23', '+', '26', ')', '/', 'animals', '*', '3', ')', '/', '(', '4', '+', '3', ')', '*', 'catdog27']]

def test_multiline_simple_expressions():
    file = io.StringIO('a + b\nc - d\np + 4\nq * 7\nnineteen * dog + 21''') 
    assert tokenizer.readlines_as_tokens(file) == [
        ['a', '+', 'b'],
        ['c', '-', 'd'],
        ['p', '+', '4'],
        ['q', '*', '7'],
        ['nineteen', '*', 'dog', '+', '21']
    ]
