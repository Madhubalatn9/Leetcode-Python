from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def createList(self, values):
        head = ListNode(values[0])
        curr = head

        for val in values[1:]:
            curr.next = ListNode(val)
            curr = curr.next

        return head
    def display(self, head):
        curr = head

        while curr is not None:
            print(curr.val, end=" -> ")
            curr = curr.next

        print("None")
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr=head
        prev=None

        while curr is not None:
            nodenext=curr.next

            curr.next=prev

            prev=curr
            curr=nodenext
        return prev

sol = Solution()


head = sol.createList([1, 2, 3, 4, 5])

print("Original:")
sol.display(head)

head = sol.reverseList(head)

print("Reversed:")
sol.display(head)
