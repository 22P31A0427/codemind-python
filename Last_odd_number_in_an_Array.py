n=int(input())
l=list(map(int,input().split()))
lst=[]
for i in range(len(l)):
    if(l[i]%2!=0):
        lst.append(l[i])
print(lst[-1])