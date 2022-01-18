import pytest
import homework


@pytest.mark.parametrize('test_input, expected',[
    (37, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]),
    (36,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]),
    (109,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107])
])
def test_primos_menores_que(test_input, expected):
    assert set(homework.primos_menores_que(test_input)) == set(expected)