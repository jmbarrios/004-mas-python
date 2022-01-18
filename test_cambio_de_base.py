import pytest
import numpy as np
from numpy.testing import assert_array_equal
import homework


@pytest.mark.parametrize('base, vector, expected',[
    (np.array([[0,1],[1,1]]), np.array([1,3]), np.array([3,4])),
    (np.array([[0,1,1],[1,0,1],[1,1,0]]), np.array([1,0,-1]), np.array([-1,0,1]))
])
def test_cambio_de_base(base, vector, expected):
    assert_array_equal(homework.cambio_de_base(base, vector), expected)

