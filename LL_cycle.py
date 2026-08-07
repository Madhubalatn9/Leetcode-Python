class solution:
    def __init__(self,val,next):
        self.val=val
        self.next=next

    def cycle(self,head:ListNode[bool]):
        slow=head
        fast=head

        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next

            if(slow == fast):
                return True
        return False

obj=solution()
