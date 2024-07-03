n=int(input("enter a number "))
pow=len(str(n))
org=n
new=0
while n>0:
    one=n%10
    new=new+(one**pow)
    n//=10
if org==new:
    print(True)
else:
    print(False) 