import json

class Palindrome():

	'''
	word:		possible palindrome.  empty string returns True
	returns:	boolean depending on palindrome validity
	'''
	@staticmethod
	def is_palindrome(word):
		if not isinstance(word, basestring):
			raise ValueError('Invalid argument type (string required)')
		
		n = len(word)
		if n < 2:
			return True
		for i in xrange(n/2):
			if word[i] != word[n-i-1]:
				return False
		return True

	'''
	file_name:	filename with data to be read
	returns:	number of palindromes in data file
	'''
	@staticmethod
	def get_number_palindromes(file_name='data.txt'):
		return len(Palindrome.get_palindrome_list(file_name=file_name))


	'''
	file_name:	filename with data to be read
	returns:	list of palindromes from data file
	'''
	@staticmethod
	def get_palindrome_list(file_name='data.txt'):
		palindromes = []
		with open(file_name, 'r') as f:
			for line in f:
				try:
					data_in = json.loads(line)
					if 'key' in data_in:
						p = data_in['key']
						if Palindrome.is_palindrome(p):
							palindromes.append(p)

				except ValueError as e: # invalid JSON
					pass

		return palindromes
