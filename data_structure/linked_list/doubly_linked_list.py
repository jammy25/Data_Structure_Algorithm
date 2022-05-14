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
    # after nth node
    def add_after(self, data, x):
        if self.head is None:
            print("Linked list is empty.")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Given node is not present in the DLL.")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
    # before nth node
    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty.")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Given node is not present in the DLL.")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

# Deletion Operation

    # at beginning
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty so can't delete any node.")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the only node present.")
        else:
            self.head = self.head.nref
            self.head.pref = None
    # at end
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty so can't delete any node.")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting the only node present.")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None
    # any node (by value)
    def delete_by_value(self, x):
        if self.head is None:
            print("Linked List is empty so can't delete any node.")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
                # print("DLL is empty after deleting the only node present.")
            else:
                print(x, "is not present in the DLL.")
            return
        if self.head.nref == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref                 #n.nref = None    n.pref = None
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print(x, "is not present in the DLL.")
                
      


DLL1 = DoublyLinkedList()
# DLL1.insert_empty(10)
DLL1.add_begin(4)
# DLL1.add_begin(14)
# DLL1.add_end(100)
# DLL1.add_after(10, 4)
DLL1.add_before(10, 4)
DLL1.delete_by_value(10)
DLL1.print_LL()
DLL1.print_LL_reverse()
