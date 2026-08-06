from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(0,n):
           nums[i]=nums[i]*nums[i]
        nums.sort()
        return nums

ob1=Solution()
ob1.sortedSquares([2,4,-2,3,])
print(ob1.sortedSquares([2,4,-2,3,]))