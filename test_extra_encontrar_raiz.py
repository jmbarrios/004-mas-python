import pytest
import homework


@pytest.mark.parametrize('f, x0, x1, tol',[
    (lambda x: -x**2 + 5, 1, 2, 1e-2),
    (lambda x: -x**2 + 5, -2, -1, 1e-2)
])
def test_encontrar_raiz(f, x0, x1, tol):
    with pytest.raises(ArithmeticError):
        homework.encontrar_raiz(f, x0, x1, tol)
