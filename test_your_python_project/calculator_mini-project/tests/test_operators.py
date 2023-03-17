from calculate.operators import Operators


def test_multiple_addtion():
    operation = "5.5 + 10 + 30 + 13.7"
    expected = 59.2
    assert Operators().addition(operation) == expected


def test_addition_with_wrong_operator():
    operation = "8 * 12"
    expected = None
    assert Operators().addition(operation) == expected


def test_addition_with_negative_numbers():
    operation = "-8 + -12"
    expected = None  # -20
    assert Operators().addition(operation) == expected


def test_addition_with_mix_signs():
    operation = "8 + 12 - 2"
    expected = None
    assert Operators().addition(operation) == expected


def test_sustraction():
    operation = "5.5 - 10 - 30 - 13.7"
    expected = -48.2
    assert Operators().subtraction(operation) == expected


def test_sustraction_with_negative_numbers():
    operation = "-8 - -12"
    expected = None  # -20
    assert Operators().subtraction(operation) == expected


def test_sustraction_with_mix_signs():
    operation = "8 - 12 + 2"
    expected = None
    assert Operators().subtraction(operation) == expected


def test_multiplication():
    operation = "5.5 * 13.7"
    expected = 75.35
    assert Operators().multiplication(operation) == expected


def test_multiplication_with_negative_numbers():
    operation = "-8 * -12"
    expected = None  # 96
    assert Operators().multiplication(operation) == expected


def test_multiplication_with_mix_signs():
    operation = "8 * 12 - 2"
    expected = None
    assert Operators().multiplication(operation) == expected


def test_division():
    operation = "5.5 / 13.7"
    expected = 0.40145985401459855
    assert Operators().division(operation) == expected


def test_division_with_negative_numbers():
    operation = "-8 / -12"
    expected = None  # 0.6666666666666666
    assert Operators().division(operation) == expected


def test_zero_division():
    operation = "8 / 0"
    expected = None
    assert Operators().division(operation) == expected
