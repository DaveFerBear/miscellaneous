import unittest
from app.palindrome import Palindrome

class TestPalindrome(unittest.TestCase):
	palindrome_test_data = 'data/test_data.txt'

	def test_palindrome_truepositive(self):
		self.assertEqual(Palindrome.is_palindrome('racecar'), True)

	def test_palindrome_truenegative(self):
		self.assertEqual(Palindrome.is_palindrome('racecars'), False)

	def test_palindrome_fileIO(self):
		self.assertEqual(Palindrome.get_palindrome_list(self.palindrome_test_data), ['racecar','qwertyxytrewq'])

if __name__ == '__main__':
	unittest.main()