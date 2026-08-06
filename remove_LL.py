class solution:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    def duplicate(self,head:ListNode[int]):
        cur=head
        while(cur is not None and cur.next is not None):
            if(cur.val==cur.next.val):
                cur.next=cur.next.next
            else:
                cur=cur.next

        return head
    def print(self,head):
        cur=head
        while(cur is not None):
            print(cur.val)
            cur=cur.next
        


head=solution(1)
head.next=solution(1)
head.next.next=solution(2)
head.next.next.next=solution(3)
head.next.next.next.next=solution(3)
dup=solution()
dup.duplicate(head)
dup.print(head)
