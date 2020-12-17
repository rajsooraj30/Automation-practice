# skip the test

import pytest

#@pytest.mark.skip
def test_meth1():
    assert True

@pytest.mark.skip(reason= "do not run test_math2")
def test_meth2():
    assert False

@pytest.mark.skipif(2>1,reason="skipped this test meth3")
def test_meth3():
    assert True