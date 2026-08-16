class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
    def add(self,data):
        if not self.root:
            self.root=Tree(data)
            return
        self.recAdd(data,self.root)
    def recAdd(self,data,node):
        if not node.left:
            node.left=Tree(data)
        elif not node.right:
            node.right=Tree(data)
        else:
            self.recAdd(data,node.left)
    def display(self,depth=0,node=None):
        if not node:
            node=self.root
        print(" "*depth,node.data)
        if node.left:
            self.display(depth+1,node.left)
        if node.right:
            self.display(depth+1,node.right)
    def remove(self,data):
        if not self.root:
            print("Tree is empty")
            return
        if self.root.data==data:
            self.root=None
            return
        self.recRemove(data,self.root)
    def recRemove(self,data,node):
        if node.left and node.left.data==data:
            node.left=None
        if node.right and node.right.data==data:
            node.right=None

        if node.left:
            self.recRemove(data,node.left)
        if node.right:
            self.recRemove(data,node.right)
    def search(self,data):
        nodefound=self.recSearch(data,self.root)

        if nodefound:
            print("true")
        else:
            print("false")
    def recSearch(self,data,node):
        if node is None:
            return None
        if  node.data==data:
            return node
        return self.recSearch(data,node.left) or self.recSearch(data,node.right)


bt=BinaryTree()
bt.add(2)
bt.add(3)
bt.add(4)
bt.add(5)
bt.add(6)
bt.add(7)
bt.display()
bt.remove(4)
print("After remove element:")
bt.display()
bt.search(9)


    