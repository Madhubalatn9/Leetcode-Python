s = "A man, a plan, a canal: Panama"
s=s.lower()
print(s)
result = "".join(filter(str.isalnum, s))
print(result)
if(result==result[::-1]):
    print("true")