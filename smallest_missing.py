


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1


        while True:
            mul=i*k
            
            if mul not in nums:
            
                return mul
            i+=1

obj=Solution()


print(obj.missingMultiple([8,2,3,4,6],2))