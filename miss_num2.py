class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            index=abs(num)-1

            if nums[index]>0:
                nums[index]=-nums[index]
        for i in range(len(nums)):
            if(nums[i]>0):
                res.append(i+1)
        return res
miss=Solution()
print(miss.findDisappearedNumbers([4,3,2,7,8,2,3,1]))