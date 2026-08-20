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
