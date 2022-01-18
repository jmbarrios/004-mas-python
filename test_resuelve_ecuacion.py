import pytest
import homework


@pytest.mark.parametrize('expected',[
    (0.734)
])
def test_resuelve_ecuacion(expected):
    assert abs(homework.resuelve_ecuacion() - expected) < 1e-2