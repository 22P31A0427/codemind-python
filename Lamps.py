n,k,x,y=map(int,input().split())
s=k*x
if x<y:
    print(s+x*(n-k))
else:
    print(s+y*(n-k))