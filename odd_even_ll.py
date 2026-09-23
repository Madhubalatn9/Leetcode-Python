# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        odd_curr=head
        even_head=head.next
        even_curr=head.next

        while even_curr and even_curr.next:
            odd_curr.next=even_curr.next
            odd_curr=odd_curr.next

            even_curr.next=odd_curr.next
            even_curr=even_curr.next
        
        odd_curr.next=even_head

        return head
#InitialiZe the LinkedList
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

obj=Solution()
res=obj.oddEvenList(head)
#Print LinkedList
while res:
    print(res.val,end='->')
    res=res.next
print("None")


