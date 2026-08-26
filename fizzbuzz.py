class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]

        for i in range(1,n+1):
            if(i%3!=0 and i%5!=0):
                ans.append(i)
            elif(i%3==0 and i%5==0 ):
                i="FizzBuzz"
                ans.append(i)
            elif(i%3==0):
                i="Fizz"
      
                ans.append(i)
            elif(i%5==0):
                i="Buzz"
                ans.append(i)
          

        str_ans=[str(x) for x in ans]
        return str_ans

obj=Solution()
print(obj.fizzBuzz(3))