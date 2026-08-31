#0-red ,1-white,2-blue
nums = [2,0,2,1,1,0]

n=len(nums)

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]>nums[j]):
            nums[i],nums[j]=nums[j],nums[i]
print(nums)