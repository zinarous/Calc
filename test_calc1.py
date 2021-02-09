import pytest
from calc_tk import calc

def test_zero(calc_entry):
    assert calc_entry == "", "Ошибка"

# @pytest.mark.parametrize("x, y, a", [(1, 2, 3), (-1, 2, 1)])
# def test_add(supply_calc, x, y, a):
#     assert supply_calc.add(x, y) == a, "Nice try!"

