class Trie:

	def __init__(self):
		self.root_node = {}

	def check_present_and_add(self, word):
		current_node = self.root_node
		is_new_Word = False

		for char in word:
			if char not in current_node:
				is_new_Word = True
				current_node[char] = {}
			current_node = current_node[char]

		if "End of Word" not in current_node:
			is_new_Word = True
			current_node["End of Word"] = {}

		return is_new_Word