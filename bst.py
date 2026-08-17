class bstNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def add(self,data):
        if not self.root:
            self.root=bstNode(data)
        self.recAdd(data,self.root)
    def recAdd(self,data,node):
        if data<node.data:
            if not node.left:
                node.left=bstNode(data)
            else:
                self.recAdd(data,node.left)
        elif data>node.data:
             if not node.right:
                 node.right=bstNode(data)
             else:
                 self.recAdd(data,node.right)
    def display(self):
        result=[]  
        self.recDisplay(self.root,result)
        print(result)
    def recDisplay(self,node,result):
        if not node:
            return None
        else:
            self.recDisplay(node.left,result)
            result.append(node.data)
            self.recDisplay(node.right,result)


bst=BST()
bst.add(45)
bst.add(10)
bst.add(50)
bst.add(9)
bst.add(11)
bst.add(46)
bst.add(51)
bst.display()