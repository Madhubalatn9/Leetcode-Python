class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected=sorted(heights)
        count=0
        for i in range(len(heights)):
            if(heights[i]!=expected[i]):
                count+=1

        return count
obj=Solution()
print(obj.heightChecker([1,1,4,2,1,3]))