class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n)[2:]
        
        inn=str(b)
        arr=[]
        count=0

        for i in range(len(inn)):
            arr.append(inn[i])
            if(arr[i]=='1'):
                count+=1
        return count
obj=Solution()

print(obj.hammingWeight(11))