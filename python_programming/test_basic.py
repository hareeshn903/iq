import unittest
from basic import reverse_string, is_prime, sum_of_digits, is_palindrome_number

class TestBasicFunctions(unittest.TestCase):

    # Test cases for reverse_string
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("racecar"), "racecar")

    # Test cases for is_prime
    def test_is_prime(self):
        self.assertTrue(is_prime(2))  # Smallest prime number
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(1))  # Not a prime number
        self.assertFalse(is_prime(0))  # Not a prime number
        self.assertFalse(is_prime(-5))  # Negative numbers are not prime
        self.assertTrue(is_prime(29))  # Prime number
        self.assertFalse(is_prime(30))  # Not a prime number

    # Test cases for sum_of_digits
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(12345), 15)  # 1+2+3+4+5 = 15
        self.assertEqual(sum_of_digits(0), 0)  # Sum of digits of 0 is 0
        self.assertEqual(sum_of_digits(9), 9)  # Single digit number
        self.assertEqual(sum_of_digits(1001), 2)  # 1+0+0+1 = 2
        self.assertEqual(sum_of_digits(987654321), 45)  # Sum of digits = 45

    # Test cases for is_palindrome_number
    def test_is_palindrome_number(self):
        self.assertTrue(is_palindrome_number(121))  # Palindrome number
        self.assertTrue(is_palindrome_number(0))  # Single-digit palindrome
        self.assertTrue(is_palindrome_number(12321))  # Odd-length palindrome
        self.assertFalse(is_palindrome_number(123))  # Not a palindrome
        self.assertFalse(is_palindrome_number(-121))  # Negative numbers are not palindromes

if __name__ == "__main__":
    unittest.main()