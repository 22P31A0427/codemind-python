n=int(input())
m=int(input())
s=0
t=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
for j in range(1,m):
    if(m%j==0):
        t=t+j
if(n==t and m==s):
    print("Amicable")
else:
    print("Not Amicable")