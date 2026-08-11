class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        separate=s.split()

        if(len(pattern)!=len(separate)):
            return False

        d1={}
        d2={}

        for a,b in zip(pattern,separate):
            if(a in d1 and d1[a]!=b):
                return False
            if(b in d2 and d2[b]!=a):
                return False
            
            d1[a]=b
            d2[b]=a
        return True
obj=Solution()
print(obj.wordPattern('abba','dog cat cat dog'))