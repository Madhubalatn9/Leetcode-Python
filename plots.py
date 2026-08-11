from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        

        flowerbed=[0]+flowerbed+[0]

        for i in range(1,len(flowerbed)-1):
            if sum(flowerbed[i-1 : i+2])==0:
                flowerbed[i]=1
                n=n-1
        return n<=0
obj=Solution()
print(obj.canPlaceFlowers([1,0,0,0,1],1))