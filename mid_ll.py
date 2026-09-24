# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        
        
       slow=head
       fast=head

       while fast and fast.next:
          slow=slow.next
          fast=fast.next.next
       return slow
    def printList(self,head_node: ListNode | None):
        curr=head_node
        
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next

        print("None")


head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
obj=Solution()
mid=obj.middleNode(head)
print("Full LinkedList:")
obj.printList(head)
print("Mid of the LinkedList:")
obj.printList(mid)


