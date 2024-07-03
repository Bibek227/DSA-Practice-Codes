n=int(input("Enter a number"))
count=0
number=n
while n>0:
    one=n%10
    if one!=0 and number%one==0:
        count+=1
    n=n//10
print(count)