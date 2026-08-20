# flowerbed=[1,0,0,0,1]
# n=1
# padding=[0]+flowerbed+[0]



# for i in range(1,len(padding)-1):
#     if sum(padding[i-1:i+2])==0:
#         padding[i]=1
#         n=n-1
# print(padding)
# if(n<=0):
#     print("true")
# else:
#     print("false")

# s="abca"
# s1=s[::-1]


# n=len(s)

# for i in range(n):
#     if(s[i]!=s1[i]):
#          print("false")
#     else:
#         print("true")


# level order
# from typing import Optional
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#        if not root:
#            return None
       

#        print(root.val,end=",")
           
      
#        self.levelOrder(root.left)
#        self.levelOrder(root.right)
       

# bt=TreeNode(3)
# left1=TreeNode(9)
# right1=TreeNode(20)

# left2=TreeNode(15)
# right2=TreeNode(7)

# bt.left=left1
# bt.right=right1
# left1.left=None
# left1.right=None
# right1.left=left2
# right1.right=right2
# tree=Solution()

# tree.levelOrder(bt)



#Pair

# arr=[1,2,3,4,5]
# k=1
# count=0

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)-1):
#         if(abs(arr[i]-arr[j])==k):
#             count+=1
# print(count)


# Binary to Integer
# list1=[1,0,1]

# bi=int("".join(map(str,list1)),2)
# print(bi)

nums=[2,1,3]

arr1=[]
arr2=[]

n=len(arr1)
m=len(arr2)

arr1.append(nums[0])

arr2.append(nums[1])
for i in range(2,len(nums)):
      if (arr1[n-1]>arr2[n-1]):
        arr1.append(nums[i])
      else:
        arr2.append(nums[i])
res=arr1+arr2
print(res)