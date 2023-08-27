a=int(input())
count=0
for i in range(2,a+1):
    v=a%i
    if v==0:
        count=count+1
if count>2:
     print("Not Prime")
else:
     print("Prime")
            
    