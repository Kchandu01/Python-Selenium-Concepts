# We can define the fixture functions in this file to make them accessible
# across multiple test files.
# when particular fixture is shared by multiple testcases then put that into conftest.py file
# Fixtures are used as setup and teardown methods for test cases
# conftest file is to generalize fixture and make it available to all test cases


import pytest


@pytest.fixture(scope='class')
def setup():
    print("Setting up environment")
    yield
    print("Fixtures completed test")


# Assume that you are building one profile page where you want to send first and last name
# and send them to your test case at run time
# here dataLoad method is fixture and

@pytest.fixture()
def dataLoad():
    print("Test case data are here")
    return ['Rocky','Bhai']

# run test case with multiple set of data


@pytest.fixture(params=[('chrome','rocky'),('firefox','jacky'),'edge','ie'])
def crossbrowser(request):
    return request.param
