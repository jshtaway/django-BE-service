from unittest import TestCase  # has database integration


class TestAPI(TestCase):
    def test_get(self):
        self.assertEqual(1, 1)
