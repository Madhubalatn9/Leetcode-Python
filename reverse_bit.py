class Solution:
    def reverseBits(self, n: int) -> int:
        b=(bin(n)[2:]).zfill(32)
        print(b)
        rev_b=b[::-1]
        print(rev_b)
        int_b=int(rev_b,2)
        print(int_b)

obj=Solution()
print(obj.reverseBits(43261596))
      