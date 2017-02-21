from unittest import TestCase

from Calculator import Calculator


class TestCalculator(TestCase):
    def test_calculator_add_method_returns_zero_empty_input(self):
        calc = Calculator()
        result = calc.add("")
        self.assertEqual(0, result)

    def test_calculator_add_method_returns_the_number_for_number_input(self):
        calc = Calculator()
        result = calc.add("2")
        self.assertEqual(2, result)

    def test_calculator_add_method_returns_the_sum_of_two_numbers(self):
        calc = Calculator()
        result = calc.add("2,3")
        self.assertEqual(5, result)

    def test_calculator_add_method_returns_the_sum_of_any_numbers(self):
        calc = Calculator()
        result = calc.add("2,3,5")
        self.assertEqual(10, result)

    def test_calculator_add_method_returns_the_sum_of_any_numbers_with_ns(self):
        calc = Calculator()
        result = calc.add("2\n3,5")
        self.assertEqual(10, result)

    def test_calculator_add_method_returns_the_sum_of_any_numbers_with_delimiters(self):
        calc = Calculator()
        result = calc.add("//;\n1;2")
        self.assertEqual(3, result)

    def test_calculator_add_fail_with_negatives(self):
        calc = Calculator()
        try:
            calc.add("//;\n1;-2")
        except Exception as e:
            self.assertEqual([-2],  e.message)

    def test_calculator_add_method_filter_greater_than_1000(self):
        calc = Calculator()
        result = calc.add("//;\n1;1100")
        self.assertEqual(1, result)
