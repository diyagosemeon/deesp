y=int(input())
n=0
while(y>0):
   x=y%10
    n=(n*10)+x
    y=y//10
print(n)
