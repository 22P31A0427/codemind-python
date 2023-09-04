n=int(input())
s=0
sq=n*n
while sq>0:
    r=sq%10
    sq=sq//10
    s=s+r
if(s==n):
        print("Neon Number")
else:
        print("Not Neon Number")