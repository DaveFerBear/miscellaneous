def find_thief(ids):
	unique_id = 0
	for id in ids:
		unique_id ^= id

	return unique_id


print find_thief([1,2,3,2,1,4,3])