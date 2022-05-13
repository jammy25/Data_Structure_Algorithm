# Class to create 'NODE'

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

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end = " ")
                n = n.nref
    
    def print_LL_reverse(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "<---", end = " ")
                n = n.pref


DLL1 = DoublyLinkedList()
DLL1.print_LL()
DLL1.print_LL_reverse()
                