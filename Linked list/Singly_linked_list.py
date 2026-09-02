class node:
			def __init__(self, data):
					self.data = data
					self.next = None

class singlylinkedlist:
			

			def __init__(self):
					self.head = None

			def is_empty(self):
				return self.head is None


			def prepend(self, data):
				new = node(data)

				if self.is_empty():
						return 'list is empty'
				
				new.next = self.head
				self.head = new


			def append(self, data):
				new = node(data)

				if self.is_empty():
						return 'List is empty'
				
				current = self.head
				while current.next is not None:
						current = current.next
				current.next = new


			def insert_after_pos(self, data, target):

				new = node(data)

				if self.is_empty():
						return 'List is empty'

				current = self.head
				while current is not None and current.data != target:
						current = current.next

				if current is None:
						return 'Target element not found in the list'

				new.next = current.next
				current.next = new


			def del_at_begin(self):
				if self.is_empty():
						return 'List is empty'
				
				self.head = self.head.next


			def del_at_end(self):
				if self.is_empty():
						return 'List is empty'
			
				if self.head.next == None:
					self.head = None

				current = self.head
				prev = None
				while current.next is not None:
					prev = current
					current = current.next

				prev.next = None


			def del_at_pos(self, target):
				
				if self.is_empty():
					return 'List is empty'

				current = self.head
				prev = None
				while current is not None and current.data != target:
					prev = current
					current = current.next

				if current is None:
					return 'target element not found'
				
				prev.next = current.next


				

				