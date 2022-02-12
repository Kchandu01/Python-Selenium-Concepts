import pytest

# Instead of writing setup in each method, wrap all methods in single class and use
# @pytest.mark.usefixtures("setup") write once and execute it for each methods.
# Here it runs before and after every test.

# If you want to run only once before the class and after all the test cases executed
# then change in conftest file @pytest.fixtures(scope = 'class')
# then it means that this fixture scope is for only class level
# class name should start with test
# Datadriven and parameterization can be done with return statements in list format
# when you define fixture scope to class only, it will run once before class is initiated and after test cases executed.


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixturedemo1(self):
        print("fixture demo-1")

    def test_fixturedemo2(self):
        print("fixture demo-2")

    def test_fixturedemo3(self):
        print("fixture demo-3")
