import unittest
from Fizzbuzzcreator import Fizzbuzzer

class FizzbuzzTestCase(unittest.TestCase):
    
    def test_fizz(self):
        self.assertEqual(Fizzbuzzer(3),"Fizz", "pas fizz")

    def test_buzz(self):
        self.assertEqual(Fizzbuzzer(5),"Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(Fizzbuzzer(15),"FizzBuzz")

    def test_normal(self):
        self.assertEqual(Fizzbuzzer(1),1)
