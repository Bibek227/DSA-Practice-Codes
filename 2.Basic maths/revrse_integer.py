n=int(input("enter a number "))
new=0
a=abs(n)
while a>0:
    one=a%10
    new=new*10+one
    a=a//10
if n<0:
    print(int("-"+str(new)))
else:
    print(new)