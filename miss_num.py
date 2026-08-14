class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(0,n+1):
         found=False
         for j in range(len(nums)):
           if(nums[j]==i):
            found=True
            break
         if not found:
          return i
        return -1 
sol=Solution()
print(sol.missingNumber([3,0,1])) 