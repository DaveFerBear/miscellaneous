def parenthesis_validator(s):
	stack = []
	s = list(s)

	otc = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

	for char in s:
		if char in ['(','[','{']:
			stack.append(char)
		elif char in [')',']','}']:
			if not stack:
				return False
			if char != otc[stack.pop()]:
				return False
	return stack == []

print parenthesis_validator(" ] ( ) }")