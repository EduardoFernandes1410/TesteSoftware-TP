from unittest import TestCase
from foo import Foo

class FooTest(TestCase):
    def test_constructor(self):
        obj = Foo()
        obj.bar()
        self.assertEqual(obj._attr, 10)

    def test_run(self):
        obj = Foo()
        self.assertEqual(obj.run(), 4)

# some comment   
