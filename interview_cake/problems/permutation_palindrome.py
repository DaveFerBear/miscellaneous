def is_potential_palindrome(s):
	s = list(s)
	unpaired_chars = set()
	for char in s:
		if char in unpaired_chars:
			unpaired_chars.remove(char)
		else:
			unpaired_chars.add(char)

	return len(unpaired_chars) <= 1


print is_potential_palindrome("ciivv")