# nums=[0,-4,19,1,8,-2,-3,5]
nums = [2,10,7,5,4,1,8,6]
max=0
min=0
j=1
for i in range(len(nums)):
    
        if(nums[i]<nums[j]):
            
            max=nums[j]
            
        if(max>nums[j]):
            max=nums[j]
            j+=1
k=1
for i in range(len(nums)):

        if(nums[i]<nums[k]):
             min=nums[i]
             k+=1
            
        if(min>nums[k]):
             min=nums[k]
             
        
print("maximum:",max,"minimum:",min)