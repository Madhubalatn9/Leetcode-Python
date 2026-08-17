nums1=[4,9,5]
nums2=[9,4,9,8,4]
ans=[]

for n in set(nums1):
    if n in nums2:
        ans.append(n)
print(ans)
        