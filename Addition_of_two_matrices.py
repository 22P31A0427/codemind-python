n=int(input())
a1=[list(map(int,input().split())) for i in range(n)]
a2=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        a1[i][j]=a1[i][j]+a2[i][j]
for i in a1:
    for j in i:
        print(j,end=' ')
    print()