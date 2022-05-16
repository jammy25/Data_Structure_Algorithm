class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

# Insertion operation

    def insert(self, data):
        if self.key is None:                      # for empty tree
            self.key = data
            return
        if self.key == data:                      # for duplicate case, it will simply ignore the duplicate value
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)          # to check which node after root node is empty on left side (Recursion)    
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

# Search Operation

    def search(self,data):
        if self.key == data:
            print("Node is found.")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree.")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in the tree.")

# Traversal Operation
    # pre-order traversal
    def preorder(self):
        print(self.key, end = " ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    # in-order traversal
    def inorder(self):        
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()
    # post-order traversal
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")

# Delete Operation

    def delete(self, data):
        if self.key is None:
            print("Tree is empty.")
            return
        if self.key > data:
            if self.lchild:                                       # To check if there is a lchild
                self.lchild = self.lchild.delete(data)            # storing the next value after deleting the asked tree
            else:
                print('Given node is not present in the tree.')
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given node is not present in the tree.")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp                                       # Both these if's are for 0 and 1 child node codition 
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:                                    # for 2 child condition
                node = self.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
            


root = BST(10)
list1 = [6, 3, 1, 6, 98, 3, 7]
for i in list1:
    root.insert(i)
# root.search(6)
# root.search(60)
print("PreOrder")
root.preorder()
print()
# print("InOrder")
# root.inorder()
# print()
# print("PostOrder")
# root.postorder()
root.delete(10)
print("After deleting:")
root.preorder()