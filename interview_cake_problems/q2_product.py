a = [1, 7, 3, 4]
b = [3, 1, 2, 5, 6, 4]
c = [1, 2, 6, 5, 9]

def get_products_of_all_ints_except_at_index(arr):
	if len(arr) == 1:
		return arr
	l = len(arr)

	before_products = [1 for x in range(len(arr))]
	after_products = [1 for x in range(len(arr))]

	cur_product = 1
	for i,n in enumerate(arr[:-1]):
		before_products[i+1] = cur_product
		cur_product*=arr[i+1]

	cur_product = 1
	for i,n in enumerate(arr[1:][::-1]):
		cur_product*=n
		after_products[l-i-2] = cur_product

	return [before_products[i]*after_products[i] for i in range(l)]

print(get_products_of_all_ints_except_at_index(c))