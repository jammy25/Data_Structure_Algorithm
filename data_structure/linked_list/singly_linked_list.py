# Class to create 'NODE'

class Node: 
    def __init__(self, data):
        self.data = data
        self.ref = None

# Class to create 'LINK' b/w Nodes

class LinkedList:
    def __init__(self):
        self.head = None

# Traversal Operation

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end = " ")            
                n = n.ref

# Adding NODE (using Node class)
    # At beginning
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    # At end
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
                n = self.head
        while n.ref is not None:
                n = n.ref
        n.ref = new_node
    # At nth position(after node)
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x  == n.data:
                break
            else:
                n = n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    # At nth position(before node)
    def add_before(self, data, x):
        # putting node before first node
        if self.head is None:                       # if node is empty          
            print("Linked list is empty.")
            return
        if self.head.data == x:                     # if nodes are present
            new_node = Node(data)
            new_node.ref = self.head                # self.add_begin(data) instead of repeating will also work 
            self.head = new_node
            return
       # putting nodes before at any position other than first position
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            else:
                n = n.ref
        if n.ref is None:
            print("Linked list not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            return
    # when list is empty
    def insert_empty(self, data):
        if self.head is None:
            self.add_begin(data)
            return            
        else:
            print("Linked list is not empty.")

# Removing Node
    # At beiginning
    def delete_begin(self):
        if self.head is None:
            print("LL is empty so we can't delete nodes!!")
        else:
            self.head = self.head.ref
    # At end
    def delete_end(self):
        if self.head is None:
            print("LL is empty so we can't delete nodes!")
        elif self.head.ref is None:                    # Elif --> handles error --> if only one node is there point head to none
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    # At any position (by value)
    def delete_by_value(self, x):
        if self.head is None:
            print("LL is empty so we can't delete nodes!")
            return
        if self.head.data == x:
            self.head = self.head.ref
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Node is not present in the LL")
            else:
                n.ref = n.ref.ref
                    

    

LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.add_begin(20)
# LL1.add_begin(50)
LL1.delete_by_value(50)
LL1.print_LL()