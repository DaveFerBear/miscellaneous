def product_of_every_other_number(num):
	product_so_far = 1
	product = []
	
	for i in xrange(len(num)):
		product.append(product_so_far)
		product_so_far *= num[i]

	product_so_far = 1
	for i in xrange(len(num)):
		product[len(num)-i-1] *= product_so_far
		product_so_far *= num[len(num)-i-1]

	return product

print product_of_every_other_number([1, 7, 3, 4])
