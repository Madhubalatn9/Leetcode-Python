class Solution:
    def reverseDegree(self, s: str) -> int:
        # res=[]
        # ans=[]
        # for i in range(len(s)):
        #     res.append(s[i])
        
        # for i in range(len(res)):
        #     d=ord(res[i])
        #     ans.append(d*(i+1))

        # ans1= sum(ans)
        # return ans1
        res=[]
        for i in range(len(s)):
            rev=26-(ord(s[i])-ord('a')+1)+1
            res.append(rev*(i+1))
        return sum(res)
            
        


            



obj=Solution()
print(obj.reverseDegree("abc"))