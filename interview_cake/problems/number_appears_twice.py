def find_abberation(nums):
	n = len(nums)-1
	total = (n*n + n)/2 * -1
	for num in nums:
		total += num

	return total

print find_abberation([1,2,4,5,6,6,3])