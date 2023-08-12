a,b,c=map(int,input().split())
s=(a+b+c)/2
t=(s*(s-a)*(s-b)*(s-c))**0.5
print(f"{t:.2f}")