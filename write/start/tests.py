from django.test import TestCase

# Create your tests here.
from django.test import TestCase
class SimpleTest(TestCase):
    def test_basic_addition(self):

    """
http://www.cnblogs.com/haozi0804/p/4660652.html
    Tests that 1 + 1 always equals 2.

    """
    self.assertEqual(1 + 1, 2)