import pytest
from zzzz import Calcul
from zzzz import validate_inp

@pytest.fixture
def calculator():
    return Calcul()

def test_parse_int(calculator):  #тест правильности парсинга строки в список
    result = list(calculator.parse('1.0+1.0'))
    expected_result = [1.0, '+', 1.0]
    assert result == expected_result, "Nice try, but you're bad at Mathematics"

def test_parse_inttofloat(calculator):  #тест парсинга привода int в float
    res = list(calculator.parse('1+1'))
    exp = [1.0, '+', 1.0]
    assert res == exp, "Nice try, but you're bad at Mathematics"

def test_line(calculator): #тест проверки парсинга введенных символов. Можно парсить только числа и симв. мат. операций.
        wrong_string = 'ABCSSS2'
        res = list(calculator.parse(wrong_string))
        exp_res = [2.0]
        assert res == exp_res, "Nice try, but you're bad at Mathematics"

@pytest.mark.parametrize('ex,reslt', [    #тест проверки просчета выражений
        ('5-2', 3.0),
        ('2+5', 7.0),
        ('2*5', 10.0),
        ('8/4', 2.0),
        ('5+2*(5-2)', 11.0)
    ])    
def test_calc(calculator, ex, reslt):
    assert calculator.calc_vivod(ex) == reslt, "Nice try, but you're bad at Mathematics"

@pytest.mark.parametrize('exp,valid',(   #тест валидатора
    ('abc', False),
    ('1+2', True),
    ('cb+2', False),
))
def test_validate(exp, valid):  
    assert validate_inp(exp) is valid, "Nice try, but you're bad at Mathematics"
