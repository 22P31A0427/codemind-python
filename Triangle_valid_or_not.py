a,b,c=map(int,input().split())
if a+b>c and b+c>a:
    print("Valid triangle")
else:
    print("Invalid triangle")