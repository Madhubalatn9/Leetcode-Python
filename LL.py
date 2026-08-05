class Node:
    def __init__(self,data):
        self.data=data
        self.pointer=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add(self,data):
        newnode=Node(data)
        if(self.head is None):
            self.head=newnode
        else:
            cur=self.head
            while(cur.pointer is not None):
                cur=cur.pointer
            cur.pointer=newnode
    def print(self):
        cur=self.head
        while(cur is not None):
            print(cur.data)
            cur=cur.pointer
    def remove(self,data):
         if(self.head is not None):
            if(self.head.data==data):
                self.head=self.head.pointer
            else:
                cur=self.head

                while(cur.pointer is not None and cur.pointer.data!=data):
                    cur=cur.pointer
                if cur.pointer is not None:
                  cur.pointer=cur.pointer.pointer
         else:
             print("Linked list is empty")
             


LL1=LinkedList()
LL1.add(1)
LL1.add(2)
LL1.add(3)
LL1.print()
LL1.remove(3)
LL1.print()