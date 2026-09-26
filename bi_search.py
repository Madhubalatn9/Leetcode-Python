class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        low=0
        high=n-1

        nums.sort()
        
        first=-1
        last=-1

        while(low<=high):
            mid=low+(high-low)//2

            if(nums[mid]==target):
                first=mid
                
                high=mid-1
            elif (nums[mid]<target):
                low=mid+1
            else:
                high=mid-1

        low=0
        high=n-1

        while(low<=high):
            mid=low+(high-low)//2

            if(nums[mid]==target):
                last=mid
                
                low=mid+1
            elif (nums[mid]<target):
                low=mid+1
            else:
                high=mid-1
            
        if first==-1:
            return []
        return list(range(first,last+1))
        
obj=Solution()

print(obj.targetIndices([1,2,3,5,2,4],2))