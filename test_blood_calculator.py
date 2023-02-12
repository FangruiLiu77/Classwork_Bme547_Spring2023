import pytest


@pytest.mark.parametrize("HDL_input, expected",
                         [(65, "Normal"),
                          (55, "Borderline Low"),
                          (20, "Low")])
def test_HDL_analysis(HDL_input, expected):
    from blood_calculator import HDL_analysis
    # arrange
    # act
    answer = HDL_analysis(HDL_input)
    # assert
    assert answer == expected


@pytest.mark.parametrize("LDL_input, expected",
                         [(265, "Very High"),
                          (135, "Borderline High"),
                          (90, "Normal")])
def test_LDL_analysis(LDL_input, expected):
    from blood_calculator import LDL_analysis
    # arrange
    # act
    answer = LDL_analysis(LDL_input)
    # assert
    assert answer == expected
