def find_kth_to_last_node(head, k):
	length = 0
	node = head
	while node:
		length += 1
		node = node.next

	if k > length:
		raise Exception("Impossible")

	t = length - k
	node = head
	while t:
		t -= 1
		node = node.next

	return node