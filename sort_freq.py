class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0

        freq={}

        for items in nums:
            freq[items]=freq.get(items,0)+1
        max1=max(freq,key=freq.get)

        return max1

obj=Solution()
print(obj.majorityElement([3,2,3]))
