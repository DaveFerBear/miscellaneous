def find_closing_parenthesis(s,n):
	s = list(s)
	count = 0
	i=n+1
	while i < len(s)-1:
		char = s[i]
		if char == '(':
			count+=1
		elif char == ')':
			count-=1
		if count == -1:
			return i
		i+=1
	raise Exception("No closing parenthesis :(")

print find_closing_parenthesis("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.",10)