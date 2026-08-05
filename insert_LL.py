#LinkedList
class node:
    def __init__(self,data):
        self.data=data
        self.pointer=None
head=node(12)
node2=node(13)
node3=node(14)


head.pointer=node2
node2.pointer=node3

cur=head

while(cur is not None):
    print(cur.data)
    cur=cur.pointer


