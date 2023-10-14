n=int(input())
s=0
d=0
l=list(map(int,input().split()))
for i in range(len(l)):
    
    if(i%2==0):
        s=s+l[i]
    if(i%2!=0):
        d=d+l[i]
a=s-d
print(a)