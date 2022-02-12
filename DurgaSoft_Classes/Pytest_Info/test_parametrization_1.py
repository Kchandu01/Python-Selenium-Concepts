import pytest


@pytest.mark.parametrize(("inputs, output"),[("10+20",30),("20+20",40)])
def test_add(inputs, output):
    assert eval(inputs) == output