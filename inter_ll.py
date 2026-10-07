from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB

        while a!=b:
            a=a.next if a else headB
            b=b.next if b else headA
        return a

if __name__ == "__main__":
    # Create the shared intersecting part: 8 -> 4 -> 5
    intersectNode = ListNode(8)
    intersectNode.next = ListNode(4)
    intersectNode.next.next = ListNode(5)

    # Create List A: 4 -> 1 -> (8 -> 4 -> 5)
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = intersectNode  # Attach the intersection

    # Create List B: 5 -> 6 -> 1 -> (8 -> 4 -> 5)
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = intersectNode  # Attach the intersection

    # Instantiate the solution and run it
    solution = Solution()
    result = solution.getIntersectionNode(headA, headB)

    # Print the result
    if result:
        print(f"Intersection found at node with value: {result.val}")
    else:
        print("No intersection found.")
