def reverse_chars(s, i, j):
	while i <= j:
		s[i],s[j] = s[j],s[i]
		i+=1
		j-=1
	return s

def reverse_words(s):
	s = list(s)
	s = reverse_chars(s, 0, len(s)-1)

	word_start = 0
	for i in xrange(len(s)+1): 
		if i == len(s) or s[i] == ' ':
			reverse_chars(s, word_start, i-1)
			word_start = i+1
	return ''.join(s)

print reverse_words("find you will pain only go you recordings security the into if")