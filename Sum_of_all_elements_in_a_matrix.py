n,m=map(int,input().split())
r=[list(map(int,input().split())) for k in range(n)]
s=0
for i in r:
    for j in i:
        s=s+j
print(s)