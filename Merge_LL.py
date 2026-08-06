
class solution:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    def merge(self ,list1:ListNode[int],list2:ListNode[int]):
          list_arr=[]
          
          while(list1 is not None):
               list_arr.append(list1.val)
               list1=list1.next
          while(list2 is not None):
               list_arr.append(list2.val)
               list2=list2.next

          list_arr.sort()

          dummy=solution(0)
          curr=dummy

          for value in list_arr:
               curr.next=solution(value)
               curr=curr.next

          return dummy.next
    def print(self,node):
         while node is not None:
            print(f"{node.val}", end="")
            if node.next is not None:
              print(" -> ", end="")
            node = node.next
         print()
              

list1=solution(1)
list1.next=solution(2)
list1.next.next=solution(4)

list2=solution(1)
list2.next=solution(3)
list2.next.next=solution(4)

merge1=solution()
res=merge1.merge(list1,list2)
merge1.print(res)
           