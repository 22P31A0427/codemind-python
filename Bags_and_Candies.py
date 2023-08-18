n,k,m=map(int,input().split())
l=k*m
if n%l==0:
    print(n//l)
else:
    print((n//l)+1)