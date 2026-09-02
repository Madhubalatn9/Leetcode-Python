class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
     
        first=-1
       
        left=0
        right=len(nums)-1

        while left<=right:
            mid=left+(right-left)//2

            if nums[mid]==target:
                first=mid
              
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
            
        left=0
        right=len(nums)-1
        last=-1

        while left<=right:
            mid=left+(right-left)//2

            if nums[mid]==target:
                last=mid
                
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
           
          
        return [first,last]

obj=Solution()
print(obj.searchRange([5,7,7,8,8,10],8))