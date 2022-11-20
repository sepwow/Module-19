import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calculator = Calculator

    def test_adding_success(self):
        assert self.calculator.adding(self, 3, 3) == 6

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 10, 2) == 8

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 3, 3) == 9

    def test_division_success(self):
        assert self.calculator.division(self, 10, 5) == 2

    def teardown(self):
        print('Выполнение метода Teardown')
