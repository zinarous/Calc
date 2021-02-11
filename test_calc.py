import pytest
from zzzz import Calcul
@pytest.mark.parametrize("x, y, a", [(1, 2, 3), (-1, 2, 1)])
def test_calc(supply_calc, x, y, Calcul.OPERATORS):
    assert supply_calc.add(x, y) == a, "Nice try, but you're bad at Mathematics"

@pytest.mark.parametrize("x, y, a", [(2, 1, 1), (4, 2, 2), (3, 2, 2)])
def test_subs(supply_calc, x, y, a):
    assert supply_calc.subtract(x, y) == a, "Nice try, but you're bad at Mathematics"

@pytest.mark.parametrize("x, y, a", [(1, 3, 3), (3, 5, 15), (2, 4, 10)])
def test_multiply(supply_calc, x, y, a):
    assert supply_calc.multiply(x, y) == a, "Nice try, but you're bad at Mathematics"

@pytest.mark.parametrize("x, y, a", [(2, 2, 1), (10, 2, 5), (3, 0, 0)])
def test_divide(supply_calc, x, y, a):
    assert supply_calc.divide(x, y) == a, "Nice try, but you're bad at Mathematics"