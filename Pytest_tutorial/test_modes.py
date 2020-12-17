import pytest

# there are different modes threw which we can run the tests
# -v denotes verbose and describe about the test more cleaerly
# -m this indicates marker
# -s this indicates that the print statements inside the test methods can be printed in the result
# -K after puttin this option we can give the substing so that only those test methods will run
# which has that substing present in the function name . also we can do concatination using and & or
# keywords between the siubstring
# eg pytest -v -k "meth or test" --> this will execute all the function having the substring "meth" or "test"
# pytest -v -k "meth and test"-->this will execute all the function having the substring "meth" and "test"
# -x this indicates that the test execution will stop after first failure . on the test result full stec trace
# will be displayed for the failed test
# --tb=no --> this indicates that the steck trace should not be displayed after using -x
# eg. pytest -v -x --tb=no
# --maxfail=n --> this indicates the nomber of failures to be run before stoping the script
# pytest -v --maxfail=2 --> this indicates that after second failure the script will stop executing
# -q --> denotes the quite mode which will remove all the unneccesary information from the test results

 
@pytest.mark.one
def test_method1():
    assert False

@pytest.mark.one
def test_method2():
    assert False

@pytest.mark.two
def test_method3():
    assert True
@pytest.mark.three
def test_method4():
    assert True

# "pytest test_modes.py -v -m one"  --> -m indicates marker

