from app import calc
from app.tests.steps_def import *
from pytest_bdd import scenario

class CalcTests():
    """Test stuff"""

    @scenario('features/unit.feature', 'Add two numbers in add function')
    def test_add_numbers(self):
        """test adding numbers"""
        pass
        # res = calc.add(5,6)
        # self.assertEqual(res, 11)