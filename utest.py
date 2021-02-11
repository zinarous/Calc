import unittest
from zzzz import Calcul
from parameterized import parameterized
from zzzz import validate_inp

class TestCalc(unittest.TestCase):


    def test_parse_int(self):  #тест правильности парсинга строки в список
        
        result = list(Calcul.parse('1.0+1.0'))
        expected_result = [1.0, '+', 1.0]
        self.assertEqual(result, expected_result, "Nice try, but you're bad at Mathematics")

    def test_parse_inttofloat(self): #тест парсинга привода int в float
        
        result = list(Calcul.parse('1+1'))
        expected_result = [1.0, '+', 1.0]
        self.assertEqual(result, expected_result, "Nice try, but you're bad at Mathematics")

    def test_line(self): #тест проверки парсинга введенных символов. Можно парсить только числа и симв. мат. операций.
        wrong_string = 'ABCSSS2'
        res = list(Calcul.parse(wrong_string))
        exp_res = [2.0]
        self.assertEqual(res, exp_res, "Nice try, but you're bad at Mathematics")
        # assert 'x' not in list(Calcul.parse(symb_res)), "Не работает"
        
    @parameterized.expand([   #тест проверки просчета выражений
        ('5-2', 3.0),
        ('2+5', 7.0),
        ('2*5', 10.0),
        ('8/4', 2.0),
        ('5+2*(5-2)', 11.0)
    ])    
    def test_calc(self, exp, reslt):
        self.assertEqual(Calcul.calc_vivod(exp), reslt, "Nice try, but you're bad at Mathematics")

    @parameterized.expand([   #тест валидатора
    ('abc', False),
    ('1+2', True),
    ('cb+2', False),
    ])
    def test_validate(self, exp, valid):  
        assert validate_inp(exp) is valid, "Nice try, but you're bad at Mathematics"
