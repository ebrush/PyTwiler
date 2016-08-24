import preprocessor

def test_listify_parens():
    tst = ['5', '7', '(', '3', '+', '(', '4', '*', '9', ')', '+', '44', ')', '7']
    preprocessor.listify_parens(tst, 2)
    assert tst == ['5', '7', ['3', '+', ['4', '*', '9', ], '+', '44'], '7']
