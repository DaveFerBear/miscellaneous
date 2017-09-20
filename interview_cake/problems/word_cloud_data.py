class WordCloudData:
	def __init__(self):
		self.word_cloud = {}

	def populate_word_cloud(self, string):
		current_word = ''
		for index,char in enumerate(string):
			if index == len(string)-1:
				if self.is_letter(char): 
					current_word+=char
				if current_word: 
					self.add_to_dictionary(current_word)

			elif char == "-":
				if index>0 and self.is_letter(string[index-1]) and self.is_letter(string[index+1]) and index<len(string)-1: 
						current_word+=char

			elif self.is_letter(char) or char == "\'":
					current_word+=char
					
			else:
				if current_word: self.add_to_dictionary(current_word)
				current_word = ''
		return self.word_cloud

	def add_to_dictionary(self, word):
		if word.lower() in self.word_cloud:
			self.word_cloud[word.lower()] += 1
		else:
			self.word_cloud[word.lower()] = 1

	def is_letter(self, char):
		return char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_letter(char):
	return char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def word_cloud_data(string):
	word_cloud = {}
	word = ''
	for index,char in enumerate(string):
		if is_letter(char):
			word += char
		else:
			if word:
				if word.lower() in word_cloud:
					word_cloud[word.lower()] += 1
				else:
					word_cloud[word.lower()] = 1
			word = ''
	return word_cloud

wc = WordCloudData()

print wc.populate_word_cloud("We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake")