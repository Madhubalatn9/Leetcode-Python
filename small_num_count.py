class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        res=[]
        count=0
        for i in range(n):
            
            count=0
            for j in range(0,i):
                if(nums[i]>nums[j]):
                    count+=1
            for j in range(i+1,n):
                if(nums[i]>nums[j]):
                    count+=1
            res.append(count)

        return res

obj=Solution()
print(obj.smallerNumbersThanCurrent([8,1,2,2,3]))