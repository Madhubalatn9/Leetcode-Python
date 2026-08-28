class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=set()
        

        for i in range(len(nums)):
            seen=set()
            for j in range(i+1,len(nums)):
                k=-(nums[i]+nums[j])
                if(k in seen ):
                    temp=tuple(sorted([nums[i],nums[j],k]))
                    res.add(temp)
                seen.add(nums[j])
                    
        return [list(t) for t in res]
obj=Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))