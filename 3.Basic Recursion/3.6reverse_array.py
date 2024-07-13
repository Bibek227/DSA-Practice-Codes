# Normal method

# arr=[1,2,3,41,5]
# newarr=[]
# for i in range(len(arr)-1,-1,-1):
#     newarr.append(arr[i])
# print(newarr)


# Recursive way

# n=[11,12,13,14,15]
# def reverseArr(n,start,end):
#     if start>end: return
#     n[start],n[end]=n[end],n[start]
#     reverseArr(n,start+1,end-1)
# print('original array',n)
# reverseArr(n,0,len(n)-1)
# print('reversed array',n)


# special array reversal

# s='a&b'
# def reverseString(s):
#     def reverseHelper(s,left,right):
#         if left>right:
#             return s
#         if not s[left].isalpha():
#            return reverseHelper(s,left+1,right)
#         if not s[right].isalpha():
#            return reverseHelper(s,left,right-1)
#         s[left],s[right]=s[right],s[left]

#         return reverseHelper(s,left+1,right-1)
#     slist=list(s)
#     reverseHelper(slist,0,len(slist)-1)
#     return ''.join(slist)   #convert list to string
# print(reverseString(s))


# Optimized way
def reverse(s):
        
        left,right=0,len(s)-1
        slist=list(s)
        
        while left<right:
            if not slist[left].isalpha():
                left+=1
            elif not slist[right].isalpha():
                right-=1
                
            else:
                slist[left],slist[right]=slist[right],slist[left]
                left+=1
                right-=1
        return ''.join(slist)
s='a@b'
print(reverse(s))
