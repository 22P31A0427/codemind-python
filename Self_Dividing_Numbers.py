a=int(input())
b=int(input())
for i in range(a,b+1):
    q=i
    c=0
    while q>0:
        r=q%10
        q=q//10
        if(r>0 and i%r==0):
            c+=1
    if(c==len(str(i))):
                print(i,end=' ')
            