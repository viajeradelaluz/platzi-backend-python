from calculate.view import View


def test_print_menu(capsys):
    View.print_menu()
    captured = capsys.readouterr()
    expected = (
        "\n=========== MENU ==========="
        "\n1 - Addition"
        "\n2 - Subtraction"
        "\n3 - Multiplication"
        "\n4 - Division"
        "\n5 - Exit"
        "\n============================\n\n"
    )
    assert captured.out == expected


def test_print_end_message(capsys):
    View.end_message()
    captured = capsys.readouterr()
    expected = "=========== GOOD-BYE ===========\n"
    assert captured.out == expected


def test_print_result(capsys):
    operation, result = "5 + 7", 12
    View.print_result(operation, result)
    captured = capsys.readouterr()
    expected = f"RESULT : {operation} = {result}\n"
    assert captured.out == expected


def test_print_result_error(capsys):
    operation, result = "5 + 7", None
    View.print_result(operation, result)
    captured = capsys.readouterr()
    expected = f"Your operation is wrong! : {operation}\n"
    assert captured.out == expected
