class LinkedListNode:

  def __init__(self, value):
    self.value = value
    self.next  = None

def reverse(head):
	if not head:
		raise Exception("Can't touch this")
	prev_node = None
	node = head
	next_node = None
	while node:
		next_node = node.next
		node.next = prev_node
		prev_node = node
		node = next_node
		
	return prev_node

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')

a.next = b
b.next = c
c.next = d

def print_list(head):
	while head:
		print head.value
		head = head.next

print_list(reverse(a))
