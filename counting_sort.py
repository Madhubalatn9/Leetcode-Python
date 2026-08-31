class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
     

      max_val=max(nums)
      min_val=min(nums)


      k=max_val-min_val+1
      count=[0]*k

      for i in nums:
        index=i-min_val
        count[index]+=1
      res=[]
      for index in range(0,len(count)):
        i=index+min_val

        freq=count[index]
   

        res.extend([i]*freq)
    
      return res

obj=Solution()
print(obj.sortArray([5,1,1,2,0,0]))