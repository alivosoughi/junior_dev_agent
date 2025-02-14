import unittest
from outputs.functions.is_prime import is_prime

class TestIsPrime(unittest.TestCase):
    def test_is_prime_with_prime_number(self):
        self.assertTrue(is_prime(5))

    def test_is_prime_with_non_prime_number(self):
        self.assertFalse(is_prime(4))

    def test_is_prime_with_one(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_with_two(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_with_negative_number(self):
        self.assertFalse(is_prime(-7))

    def test_is_prime_with_zero(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_with_large_prime_number(self):
        self.assertTrue(is_prime(7919))

    def test_is_prime_with_large_non_prime_number(self):
        self.assertFalse(is_prime(7920))

if __name__ == '__main__':
    unittest.main()