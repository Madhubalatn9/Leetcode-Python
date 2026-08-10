import typing
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head:typing.Optional[ListNode]) -> typing.Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:

            first = prev.next
            second = first.next

            # Relink the nodes
            first.next = second.next
            second.next = first
            prev.next = second

            # Move to the next pair
            prev = first

        return dummy.next

    
    def print(self,node):
             while node is not None:
                print(f"{node.val}",end="")
                if node.next is not None:
                    print(" -> ",end="")
                node = node.next
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)

swap=Solution()
res=swap.swapPairs(head)
swap.print(res)
