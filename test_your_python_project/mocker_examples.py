import time

from mocker_modules import request_call

PI = 3.1415

# **********************
#   Mocking a constant
# **********************


def circumference(radius):
    """Calculate the circumference of a circle."""
    return 2 * PI * radius


def test_return_circumference(mocker):
    """Test example to mock a constant."""
    mocker.patch.object(circumference, "PI", 3.14)

    expected_value = 62.83
    assert circumference(10) == expected_value


# **********************
#   Mocking a function
# **********************


def request():
    """Request a web page."""
    time.sleep(5)
    return 10


def test_request_call(mocker):
    """Test example to mock a function."""
    mocker.patch("request_call.request", return_value=100)

    exepted_value = 100
    assert request_call() == exepted_value
