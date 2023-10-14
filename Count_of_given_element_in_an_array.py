n=int(input())
c=0
l=list(map(int,input().split()))
a=int(input())
for i in l:
    if(i==a):
        c=c+1
print(c)