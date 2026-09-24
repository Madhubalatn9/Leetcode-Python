class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)):
            n_first=nums[i]%10
            n_last=nums[i]//10

            if abs(n_first)+n_last==i:
                res.append(i)
        if res is not None: 
            return  min(res)
        else: 
            return -1

obj=Solution()
print(obj.smallestIndex([1,3,2]))