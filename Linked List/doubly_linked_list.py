# Class to create 'NODE'

from tkinter import N


class Node:
    def __init__ (self, data):
        self.data = data
        self.nref = None
        self.pref = None

# Class to create 'LINK' b/w Nodes

class DoublyLinkedList:
    def __init__ (self):
        self.head = None

# Traversal Operation
    #Traversing in forward direction
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end = " ")
                n = n.nref
    #Traversing in reverse direction
    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("Linked List is empty.")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "--->", end = " ")
                n = n.pref

# Insertion Operation
    # if list is empty
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty.")
    # at beginning
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    # at end
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            new_node.pref = n
            n.nref = new_node




DLL1 = DoublyLinkedList()
# DLL1.insert_empty(10)
# DLL1.add_begin(20)
DLL1.add_end(100)
DLL1.print_LL()
DLL1.print_LL_reverse()
                