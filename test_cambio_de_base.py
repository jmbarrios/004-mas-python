import pytest
import homework


@pytest.mark.parametrize('base, vector, expected',[
    ([[0,1],[1,1]], [1,3], [2,1]),
    ([[0,1,1],[1,0,1],[1,1,0]], [1,0,-1], [-1,0,1])
])
def cambio_de_base(base, vector, expected):
    assert homework.cambio_de_base(base, vector) == expected