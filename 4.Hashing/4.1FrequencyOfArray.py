# Frequencies of Limited Range Array Elements

n=5
arr=[2,3,2,3,5]
p=5
# Output: 0 2 2 0 1
# Explanation: Counting frequencies of each array element We have: 1 occurring 0 times. 2 occurring 2 times. 3 occurring 2 times. 4 occurring 0 times. 5 occurring 1 time.
res=[]

for i in range(1,n+1):
    count=0
    for j in range(len(arr)):
            if i==arr[j]:
                count+=1
    res.append(count)

print(res)