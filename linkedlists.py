class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

def has_cycle(root):
	fast, slow = root, root
	while fast is not None and fast.next is not None:
		fast = fast.next.next
		slow = slow.next

		if fast == slow:
			return True
			
	return False