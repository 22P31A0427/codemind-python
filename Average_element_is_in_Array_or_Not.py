n=int(input())
l=list(map(int,input().split()))
avg=sum(l)//n
print(avg in l)