n=int(input())
s=0
while(n):
    r=n%10
    n=n//10
    s=s*10+r
print(s)