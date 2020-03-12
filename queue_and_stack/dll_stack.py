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
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        self.size -= 1
        value = self.storage.remove_from_tail()
        return value

    def len(self):
        return self.size
