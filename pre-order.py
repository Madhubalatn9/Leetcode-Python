class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preOrderTraversal(node):
        if not node:
            return 
        print(node.data , end=",")
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)
def inOrderTraversal(node):
     if not node:
          return
     inOrderTraversal(node.left)
     print(node.data,end=",")
     inOrderTraversal(node.right)
def postOrderTraversal(node):
     if not node:
          return
     postOrderTraversal(node.left)
     postOrderTraversal(node.right)
     print(node.data,end=",")

root=TreeNode('R')
a=TreeNode('A')
b=TreeNode('B')
c=TreeNode('C')
d=TreeNode('D')
e=TreeNode('E')
f=TreeNode('F')
g=TreeNode('G')

root.left=a
root.right=b

a.left=c
a.right=d

b.left=e
b.right=f

f.left=g


print("Pre-Order:")
preOrderTraversal(root)
print("\nIn-Order:")
inOrderTraversal(root)
print("Post-Order:")
postOrderTraversal(root)



