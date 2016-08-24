import evaluator

def test_evaluations_and_assignments():
    a = ['testvar', '=', 'testvar2', '=', [7, '-', 3, '+', 9, '*', 7], '*', 3, '*', [2, '+', 3], '*', [4, '+', 2], '/', 2]
    assert evaluator.e(a) == 3015
    assert evaluator.testvar == 3015
    assert evaluator.testvar2 == 3015

    b = ['anothervar', '=', 'testvar2', '*', 5]
    assert evaluator.e(b) == 15075
    assert evaluator.anothervar == 15075
    assert evaluator.testvar == 3015
    assert evaluator.testvar2 == 3015

    c = ['anothervar', '=', 'anothervar', '*', 2]
    assert evaluator.e(c) == 30150
    assert evaluator.anothervar == 30150
