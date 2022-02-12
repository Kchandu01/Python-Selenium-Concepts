# Any Pytest File should start with test_ or end with _test
# Test method name must start with test_
# Any code should be wrapped in method and method name should have sense(meaning)
# -k stands for method names execution, -s logs in output, -v for more data
# you can mark (tag) tests and then run with -m
import pytest


@pytest.mark.xfail
def test_firstProgram(setup):
    print("hello")


@pytest.mark.skip(" This test is going to fail")
def test_verifyCreditcard():
    a= 2
    b= 6
    assert a+3 == b
