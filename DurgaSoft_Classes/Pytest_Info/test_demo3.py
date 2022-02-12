import pytest


@pytest.mark.xfail
def test_loginCreditcard():
    print("xfail test")
    string = 'Hello'
    assert string == 'Hi'

"""
@pytest.mark.xfail : 
    When you give this particular test will run but in output you wont see pass or failed status.
    Just running but not reporting.
"""