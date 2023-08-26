a=int(input())
sum=0
for i in range(1,a,1):
    b=a%i
    if(b==0):
        sum=sum+i
if sum==a:
    print("True")
else:
    print("False")