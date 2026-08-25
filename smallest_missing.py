nums = [8,2,3,4,6]
k = 2
num_set=set(nums)
print(num_set)
i=1


while True:
    mul=i*k
    
    if mul not in num_set:
        print(mul)
        break
    i+=1