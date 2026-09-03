class node:
               def __init__(self, data):
                              self.data = data
                              self.next = None
                              self.prev = None

class doubly_linked_list:
                def __init__(self):
                       self.head = None
                       self.tail = None

                def is_empty(self):
                        return self.head == 0

                def prepend(self, data):
                       new = node (data)

                       if self.is_empty():
                               return 'List is empty'

                       new.next = self.head
                       self.head.prev = new
                       self.head = new
                       