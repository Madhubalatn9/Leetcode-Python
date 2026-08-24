
# climbing step
n=2
prev1=0
prev=1

for _ in range(n):
  prev1,prev=prev,prev1+prev
print (prev)