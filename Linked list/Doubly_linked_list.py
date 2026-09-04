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
                        return self.head is None or self.tail is None

                def prepend(self, data):
                       new = node (data)

                       if self.is_empty():
                               self.head = new
                               self.tail = new
                               return 

                       new.next = self.head
                       self.head.prev = new
                       self.head = new
        

                def append(self, data):
                        new = node(data)

                        if self.is_empty():
                                self.head = new
                                self.tail = new
                                return

                        self.tail.next = new
                        new.prev = self.tail
                        self.tail = new

                def insert_after_pos(self, data, target):
                        new = node(data)

                        if self.is_empty():
                                return 'List is empty'

                        current = self.head
                        while current is not None and current.data != target:
                                current = current.next

                        if current is None:
                                return ' Target elemnet not found in the list'

                        new.prev = current
                        new.next = current.next

                        if current.next.prev is not None:
                                current.next.prev = new

                        current.next = new

                



                                

                
                
                       