class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max1=max(nums)
        for i in range(len(nums)):
            if(nums[i]==max1):
                return i
obj=Solution()
print(obj.findPeakElement([1,2,3,1]))