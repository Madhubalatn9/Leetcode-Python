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

# nums=[2,1,3]

# arr1=[]
# arr2=[]

# n=len(arr1)
# m=len(arr2)

# arr1.append(nums[0])

# arr2.append(nums[1])
# for i in range(2,len(nums)):
#       if (arr1[n-1]>arr2[n-1]):
#         arr1.append(nums[i])
#       else:
#         arr2.append(nums[i])
# res=arr1+arr2
# print(res)

# nums = [4,3,2,7,8,2,3,1]

# res=[]
# for i in range(0,len(nums)+1):
#     found=False
    
#     if(nums[i]==j):
#         found=True
#         break
            
#     if found==False:
#         res.append(i)
# print(res)

# nums = [1,3,4,2,2]

# for i in range(0,len(nums)):
#     for j in range(i+1,len(nums)):
#         if(nums[i]==nums[j]):
#             print(nums[i])
       
# s = "A man, a plan, a canal: Panama"
# s=s.lower()
# print(s)
# result = "".join(filter(str.isalnum, s))
# print(result)
# if(result==result[::-1]):
#     print("true")

# s = "pwwwke"
# li=list(s)
# print(li)
# res=set(li)
# print(res)
# print(len(res))

# num1=[1,2,2,1]
# num2=[2,2]

# for i in range(len(num1)):
#     for j in range(len(num2)):
#         if(num1[i]==num2[j]):
#             print(num1[i])

# Run this in Python to get the exact 10,000 element array string
# 
# Generate a 1,000-element list string (well under character limits)
# 
# print(list(range(1, 1001)))
# n=10
# original=n

# digit=[]
# while original>0:
#  digit.insert(0,original%10)

#  original//=10
 
# for i in range(len(digit)):
#    for j in range(1,len(digit)):
#      sum=digit[i]+digit[j]
#      product=digit[i]*digit[j]
#      if(sum+product==n):
#       print("true")
#      else:

#       print("false")
# print (digit)

# 3 Sum

# nums = [-1,0,1,2,-1,-4]
# res=[]

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         for k in range(j+1,len(nums)):
#             if(nums[i]+nums[j]+nums[k]==0):
#                 res.append([nums[i],nums[j],nums[k]])
                
#             print(res)


#climbing step
# n=2
# prev1=0
# prev=1

# for _ in range(n):
#   prev1,prev=prev,prev1+prev
# print (prev)

# print(ord('💐'))

# charTitle=1
# result=0

# char_value=charTitle-ord('A')+1
# result=result*26+ char_value
# print()    

# nums = [8,2,3,4,6]
# k = 2
# num_set=set(nums)
# print(num_set)
# i=1


# while True:
#     mul=i*k
    
#     if mul not in num_set:
#         print(mul)
#         break
#     i+=1


 
# s = "IceCreAm"
# vowels="aeiouAEIOU"

# if any(char in vowels for char in s) :
#     reverse=vowels[::-1]
#     print(reverse)

n=3

ans=[]

for i in range(1,n+1):
   if(i%3!=0 or i%5!=0):
      ans.append(i)
   elif(i%3==0 and i%5==0 ):
      i="FizzBuzz"
      ans.append(i)
   elif(i%3==0):
      i="Fizz"
      print(i)
      ans.append(i)
   elif(i%5==0):
      i="Buzz"
      ans.append(i)
   

str_ans=[str(x) for x in ans]

print(str_ans)
      
      
    

   