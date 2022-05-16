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
    # post-order
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")




root = BST(20)
list1 = [20, 4, 30, 4, 1, 5, 6]
for i in list1:
    root.insert(i)
root.search(6)
root.search(60)
print("PreOrder")
root.preorder()
print()
print("InOrder")
root.inorder()
print()
print("PostOrder")
root.postorder()