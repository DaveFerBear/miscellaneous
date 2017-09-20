def all_permutations(rem_list): #recursive 
	
	if len(rem_list) == 1:
		return set([s])

	local_set = set()

	length = len(rem_list)
	for index in xrange(length):
		copy_s = rem_list[:]
		current = copy_s.pop(index)
		items = all_permutations(copy_s)
		for item in items:
			item.append(current)
			local_set.append(item)

	return local_set

def perms(word): #iterative
  stack = list(word)
  results = [stack.pop()]
  while len(stack) != 0:
    c = stack.pop()
    new_results = []
    for w in results:
      for i in range(len(w)+1):
        new_results.append(w[:i] + c + w[i:])
    results = new_results
  return results

print len(all_permutations(list("abcd")))

# "abc"
# "acb"
# "bac"
# "bca"
# "cab"
# "cba"