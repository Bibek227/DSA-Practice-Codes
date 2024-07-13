# Normal method

# arr=[1,2,3,41,5]
# newarr=[]
# for i in range(len(arr)-1,-1,-1):
#     newarr.append(arr[i])
# print(newarr)


# Recursive way
n=[11,12,13,14,15]
def reverseArr(n,start,end):
    if start>end: return
    n[start],n[end]=n[end],n[start]
    reverseArr(n,start+1,end-1)
print('original array',n)
reverseArr(n,0,len(n)-1)
print('reversed array',n)

