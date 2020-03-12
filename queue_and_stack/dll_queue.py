import sys
sys.path.append('/Users/dxtrlws/Lambda/Computer Science/03 Data Structures/Lectures/Data-Structures/doubly_linked_list/')
from doubly_linked_list import DoublyLinkedList



class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        self.size -=1
        self.storage.remove_from_head()

    def len(self):
        return self.size
