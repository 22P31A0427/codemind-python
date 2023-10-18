n=int(input())
s=n*n
c=0
while(n>0):
    if(s%10!=n%10):
        print("Not an Automorphic Number")
        c=1
        break
    n=n//10
    s=s//10
if(c==0):
    print("Automorphic Number")