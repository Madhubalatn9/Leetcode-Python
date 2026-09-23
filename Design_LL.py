class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class MyLinkedList:

    def __init__(self):
        self.head=None
    

    def get(self, index: int) -> int:
        curr=self.head
        i=0
        while curr:
            if i==index:
                return curr.val
            curr=curr.next
            i+=1
        return -1

            


    def addAtHead(self, val: int) -> None:
        curr=self.head
        new_node=ListNode(val)
        new_node.next=curr
        self.head=new_node

    def addAtTail(self, val: int) -> None:
        new_node=ListNode(val)

        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_node

    def addAtIndex(self, index: int, val: int) -> None:
            if index == 0:
              self.addAtHead(val)
              return

            curr = self.head
            i = 0

            while curr and i < index - 1:
                curr = curr.next
                i += 1

            if curr is None:
                return

            new_node = ListNode(val)

            new_node.next = curr.next
            curr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
         return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        i = 0

        while curr and i < index - 1:
            curr = curr.next
            i += 1

        if curr is None or curr.next is None:
            return

        curr.next = curr.next.next
    def print_list(self):
        curr = self.head

        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next

        print("None")


head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
obj=MyLinkedList()
obj.head=head
print("Initial:")

obj.print_list()
print("get value:")
print(obj.get(1))
print("Add Value at head:")
obj.addAtHead(0)
obj.print_list()
print("Add Value at Tail:")
obj.addAtTail(5)
obj.print_list()
print("Add Value at specific index:")
obj.addAtIndex(1,10)
obj.print_list()
print("delete value at specific index")
obj.deleteAtIndex(2)
obj.print_list()
res=obj.head

