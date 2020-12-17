# parameterization helps to run number of steps with the same function

import pytest

def add(x,y):
    return x+y
@pytest.mark.parametrize('num1,num2,result',
                         [(7,3,10),
                          ('Hello','World','HelloWorld'),
                          (10.5,25.5,36)])
def test_meth(num1,num2,result):
    assert add(num1,num2)==result
