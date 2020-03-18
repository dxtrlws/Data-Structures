import sys
sys.path.append('/Users/dxtrlws/Lambda/Computer Science/03 Data Structures/Lectures/Data-Structures/doubly_linked_list/')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size +=1
        self.storage.add_to_head(value)

    def pop(self):
        if self.len() > 0:
            self.size -=1
            return self.storage.remove_from_head()
        else:
            return

    def len(self):
        return len(self.storage)
