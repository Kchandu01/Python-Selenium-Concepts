# How to run testcases with multiple set of data's

import pytest


def test_crossbrowser(crossbrowser):
    print(crossbrowser)
    # to print rocky for first run and jacky for second run , d and e
    print(crossbrowser[1])


# After running this test it will run for 4 times