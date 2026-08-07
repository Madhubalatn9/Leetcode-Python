from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
       arr1=[]
       arr2=[]
       while(l1 is not None):
          arr1.append(l1.val)
          l1=l1.next
       while(l2 is not None):
           arr2.append(l2.val)
           l2=l2.next
   
       val1="".join(map(str,arr1))
       val2="".join(map(str,arr2))

       rev_val1=int(val1[::-1])
       rev_val2=int(val2[::-1])

       add=rev_val1+rev_val2

       ans=(str(add)[::-1])

       dummy=ListNode(0)
       curr=dummy

       for value in ans:
           curr.next=ListNode(int(value))
           curr=curr.next

       return dummy.next


    def print(self,node):
         while node is not None:
            print(f"{node.val}",end="")
            if node.next is not None:
                print(" -> ",end="")
            node = node.next
            
        

l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)

l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4) 

add1=Solution()
res=add1.addTwoNumbers(l1,l2)
add1.print(res)





       