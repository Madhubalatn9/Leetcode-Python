


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1


        while True:
            mul=i*k
            
            if mul not in nums:
            
                return mul
            i+=1

obj=Solution()

obj1=obj.missingMultiple(3)
print(obj.missingMultiple(3))