from django.test import SimpleTestCase  # no database integration, but has django integration
from app.calc import add


class TestCalc(SimpleTestCase):

    def test_add(self):
        res = add(3, 8)
        self.assertEqual(res, 11)
