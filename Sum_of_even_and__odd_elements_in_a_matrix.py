n,m=map(int,input().split())
r=[list(map(int,input().split())) for k in range(n)]
e=0
o=0
for i in r:
    for j in i:
        if(j%2==0):
            e=e+j
        elif(j%2!=0):
            o=o+j
print(f"{e} {o}")
