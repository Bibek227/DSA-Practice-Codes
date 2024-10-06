# Input: array[] = {10,5,10,15,10,5};
# Output: 10 15
# Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

arr=[10,5,10,15,10,5]
l=[]
for i in range(len(arr)):
    c=arr.count(arr[i])
    l.append(c)
m1=max(l)
m2=min(l)
i1=l.index(m1)
i2=l.index(m2)
print(arr[i1],arr[i2])