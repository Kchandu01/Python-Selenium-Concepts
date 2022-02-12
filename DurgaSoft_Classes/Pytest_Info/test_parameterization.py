import pytest


# A simple addition function that adds/concatenates two input values
def add_operation(input_1, input_2):
    return input_1 + input_2


# We make use of to parametrize decorator to supply input arguments
# to the test function

@pytest.mark.parametrize('inp_1,inp_2,result', [(9, 6, 15), (10, 20, 30)])
def test_add_integers_strings(inp_1, inp_2, result):
    result_1 = add_operation(inp_1, inp_2)
    assert result_1 == result
