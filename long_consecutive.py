class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        max1=1
        count=1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=1
                if count>max1:
                    max1=count
            else:
                count=1

        return max1      

obj=Solution()
print(obj.findLengthOfLCIS([1,3,5,4,6]))          