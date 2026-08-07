from typing import Optional
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        while(head is not None):
            list1.append(head.val)
            head=head.next

        for i in range(1,len(list1)):
            curr=list1[i]
            j=i-1

            while(j>=0 and curr<list1[j]):
                list1[j+1]=list1[j]
                j-=1
            list1[j+1]=curr

        dummy=ListNode(0)
        curr=dummy

        for i in list1:
            curr.next=ListNode(i)
            curr=curr.next

        return dummy.next
    def print(self,node):
             while node is not None:
                print(f"{node.val}",end="")
                if node.next is not None:
                    print(" -> ",end="")
                node = node.next 
head=ListNode(4)
head.next=ListNode(2)
head.next.next=ListNode(1)
head.next.next.next=ListNode(3)

insert=Solution()
res=insert.insertionSortList(head)
insert.print(res)
