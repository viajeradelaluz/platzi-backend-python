from calculate.operators import Operators


def test_make_multiple_addtion():
    run = Operators()
    operation = "5.5 + 10 + 30 + 13.7"
    expected = 59.2
    assert run.addition(operation) == expected
