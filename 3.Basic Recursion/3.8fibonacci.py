# n1=0
# n2=1
# n3=0
# sum=0
# n=int(input('enter a range '))
# print(n1,end=' ')
# for i in range(1,n):  
#     n1=n2
#     n2=n3
#     n3=n1+n2
#     print(n3,end=' ')
#     sum=n2+n3
# print('sum=',sum)



# using recursion
def fibonaci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)
def sum_fibonaci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonaci(n)+sum_fibonaci(n-1)
n=int(input('enter a range '))
for i in range(n):
    print(fibonaci(i),end=' ')
print('\nsum=',sum_fibonaci(n-1))