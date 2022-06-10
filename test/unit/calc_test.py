import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation_true(*args, **kwargs):
    return True

class InvalidPermissions(Exception):
    pass

@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
## Pruebas del metodo add caso de exito
    def test_add_method_returns_correct_result(self):
        self.assertEqual(5, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
## Pruebas del metodo substract caso de exito
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.substract(3, 2))
        self.assertEqual(6, self.calc.substract(3, -3))
        self.assertEqual(-6, self.calc.substract(-3, 3))
## Pruebas del metodo multiply caso de exito
    @patch('app.util.validate_permissions', side_effect=mocked_validation_true, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
## Pruebas del metodo multiply caso de exito
    def test_multiply_method_returns_correct_result_no_permissions(self):
        self.assertRaises(TypeError, self.calc.multiply, 2, 0, "user")

## Pruebas del metodo divide caso de exito
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
## Pruebas del metodo divide caso de fallo division para cero
    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)
## Pruebas del metodo power caso de exito
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(0.0009765625, self.calc.power(-2, -10))
        self.assertEqual(1024, self.calc.power(2, 10))
        self.assertEqual(1, self.calc.power(0, 0))
        self.assertEqual(1, self.calc.power(3, 0))
        self.assertEqual(1, self.calc.power(1, 10))
## Pruebas del metodo sqrt caso de exito
    def test_sqrt_method_fails_with_numbers_less_than_zero(self):
        self.assertRaises(TypeError, self.calc.sqrt,-3)
        self.assertRaises(TypeError, self.calc.sqrt, "-3")
## Pruebas del metodo sqrt caso de exito
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.sqrt(0))
        self.assertEqual(3, self.calc.sqrt(9))
        self.assertEqual(5, self.calc.sqrt(25))
        self.assertEqual(1.772455923288362, self.calc.sqrt(3.1416))
## Pruebas del metodo log10 caso de exito
    def test_log10_method_fails_with_numbers_less_than_zero(self):
        self.assertRaises(TypeError, self.calc.log10,-3)
        self.assertRaises(TypeError, self.calc.log10, "-3")
        self.assertRaises(TypeError, self.calc.log10, 0)
## Pruebas del metodo log10 caso de exito
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.log10(1))
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(2, self.calc.log10(100))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
