n=int(input('enter a number '))
original=n
new=0
a=abs(n)
while a>0:
    one=a%10
    new=new*10+one
    a=a//10
if new==original and n>0:
    print(True)
else:
    print(False)
