import pytest


@pytest.mark.parametrize("input, expected", [
    ([(3, 5), (4, 7), 2], 3),
])
def test_y_finder(input, expected):
    from in_class_exercise_0203 import y_finder
    answer = y_finder(input)
    assert answer == expected
