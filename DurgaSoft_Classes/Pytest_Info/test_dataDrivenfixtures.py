# How parameterization can be achieved for tests with multiple sets of data
# How to drive data for your test case
# fixtures is not only to run pre-requisite it will also help you to load data, that also pre-requisite
# to run test (ex: while working on user page you want to put user details name, email etc)
# class name should start with test
import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editprofile(self, dataLoad):
        # when it is returning something it is mandatory to pass that fixture name into method
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])

"""
Interview question:
In what scenario you will be forced to pass fixture name though you have declared globally?
Ans: 
when you are returning something then you should have argument of your fixture name
"""