a,b=map(int,input().split())
count=0
for i in range(1,b+1):
    if(i*a%b==0):
        print(i*a)
        break