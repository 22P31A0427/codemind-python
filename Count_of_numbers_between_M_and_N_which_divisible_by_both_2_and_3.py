a,b=map(int,input().split())
count=0
for i in range(a,b,1):
    d=i%2
    e=i%3
    if d==0 and e==0:
        count+=1
print(count)