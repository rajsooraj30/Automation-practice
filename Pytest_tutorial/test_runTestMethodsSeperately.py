import pytest

def test_meth1():
    assert True

def test_meth2():
    assert True

def test_meth3():
    assert False


# to run the test seperately for particular method in a test file we can run as
# "pytest test_runTestMethodsSeperately.py::test_meth1"
# -v can be used for more information
# -k can be used to provide the substring of an function and run that perticular function
# eg: pytest -v -k meth1    --> run the meth1 function from whole folder# pytest test_runTestMethodsSeperately.py -v -k meth1 --> run the meth1 function from this module


