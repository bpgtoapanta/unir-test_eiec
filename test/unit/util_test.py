import unittest
import pytest

from app import util


@pytest.mark.unit
class TestUtil(unittest.TestCase):
    def test_convert_to_number_correct_param(self):
        self.assertEqual(4, util.convert_to_number("4"))
        self.assertEqual(0, util.convert_to_number("0"))
        self.assertEqual(0, util.convert_to_number("-0"))
        self.assertEqual(-1, util.convert_to_number("-1"))
        self.assertAlmostEqual(4.0, util.convert_to_number("4.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("0.0"), delta=0.0000001)
        self.assertAlmostEqual(0.0, util.convert_to_number("-0.0"), delta=0.0000001)
        self.assertAlmostEqual(-1.0, util.convert_to_number("-1.0"), delta=0.0000001)

    def test_convert_to_number_invalid_type(self):
        self.assertRaises(TypeError, util.convert_to_number, "")
        self.assertRaises(TypeError, util.convert_to_number, "3.h")
        self.assertRaises(TypeError, util.convert_to_number, "s")
        self.assertRaises(TypeError, util.convert_to_number, None)
        self.assertRaises(TypeError, util.convert_to_number, object())

    ## Pruebas del metodo check_types caso de fallo
    def test_check_types_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, util.check_types, "2", 2)
        self.assertRaises(TypeError, util.check_types, 2, "2")
        self.assertRaises(TypeError, util.check_types, "2", "2")
        self.assertRaises(TypeError, util.check_types, None, 2)
        self.assertRaises(TypeError, util.check_types, 2, None)
        self.assertRaises(TypeError, util.check_types, object(), 2)
        self.assertRaises(TypeError, util.check_types, 2, object())

    ## Pruebas del metodo check_type caso de fallo
    def test_check_type_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, util.check_type, "2")
        self.assertRaises(TypeError, util.check_type, None)
        self.assertRaises(TypeError, util.check_type, object())

    ## Pruebas del metodo validate_permissions caso de fallo
    def test_validate_permissions_method(self):
        self.assertTrue(util.validate_permissions("oper", "user1"))
