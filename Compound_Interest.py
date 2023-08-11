p=int(input())
t=int(input())
r=int(input())
ci=p*((1+(t/100))**r)
c=ci-p
print(f"{c:.2f}")
