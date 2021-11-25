from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock, patch

class B:
    @staticmethod
    def f(x):
        return int(x)

class A:
    def __init__(self):
        pass

    def run(self):
        return (2)*B.f('132131').example()

class OutputManagerTest(TestCase):

    def test_output_manager(self):
        self.assertFalse(False)

    def test_init(self):
        mock_print = MagicMock()
        with patch.object(B, 'f')  as mock_print:
            mock_print.return_value.example.return_value = 4
            a = A()
            self.assertEqual(a.run(), 8)