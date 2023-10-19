import pytest
from TP_5_Funciones import *

@pytest.mark.parametrize("a, b, res",[
    (2,4,6),
    (-4,6,2),
    (-5,-1,-6),
])
def test_suma(a,b,res):
    assert suma(a,b) == res 
    