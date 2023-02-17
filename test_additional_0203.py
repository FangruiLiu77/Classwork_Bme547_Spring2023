import pytest


@pytest.mark.parametrize("input, expected", [
    ([(3, 5), (4, 7), (2, 3)], True),
    ([(2, 7), (3, 10), (5, 19)], False)
])
def test_y_finder(input, expected):
    from additional_0203 import y_checker
    answer = y_checker(input)
    assert answer == expected
