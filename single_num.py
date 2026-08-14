class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0

        for num in nums:
          res^=num
        return res

sol=Solution()

print(sol.singleNumber([1,0,1]))


