import unittest
from Fizzbuzzcreator import Fizz
from Fizzbuzzcreator import Buzz
from Fizzbuzzcreator import Bang
from Fizzbuzzcreator import Fizzbuzzbang


class FizzbuzzTestCase(unittest.TestCase):
    
    def test_fizz(self):
        self.assertEqual(Fizz(3),"Fizz")
    def test_buzz(self):
        self.assertEqual(Buzz(5),"Buzz")
    def test_bang(self):
        self.assertEqual(Bang(7),"Bang")
    def test_fizzbuzz(self):
        self.assertEqual(Fizzbuzzbang(15),"FizzBuzz")
    def test_fizzbuzzbang(self):
        self.assertEqual(Fizzbuzzbang(105),"FizzBuzzBang")

"""
     def test_(self):
        self.assertEqual(Fizzbuzzer(35),"Bang")

    def test_fizz(self):
        self.assertEqual(Fizzbuzzer(3),"Fizz", "pas fizz")

    def test_buzz(self):
        self.assertEqual(Fizzbuzzer(5),"Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(Fizzbuzzer(15),"FizzBuzz")

    def test_normal(self):
        self.assertEqual(Fizzbuzzer(1),1)
"""
