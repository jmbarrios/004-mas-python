import pytest
import homework


@pytest.mark.parametrize('f, x0, x1, tol, expected',[
    (lambda x: -x**2 + 5, -3, 1/2, 1e-2, -2.234),
    (lambda x: -x**2 + 5, 1/2, 5, 1e-2, 2.234),
    (lambda x: x**3 + x**2 - 1, 0, 1, 1e-3, 0.7546)
])
def test_encontrar_raiz(f, x0, x1, tol, expected):
    assert abs(homework.encontrar_raiz(f, x0, x1, tol) - expected) < tol