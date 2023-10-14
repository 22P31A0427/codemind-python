n=int(input())
l=list(map(int,input().split()))
s=0
d=0
for i in range(len(l)):
    if(l[i]%2==0):
        s=s+l[i]
    if((l[i]%2!=0)):
        d=d+l[i]
a=abs(s-d)
print(a)