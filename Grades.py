a,b,c,d,e=map(int,input().split())
n=(a+b+c+d+e)//5
if n>=90:
    print("Grade A")
elif n>=80:
    print("Grade B")
elif n>=70:
    print("Grade C")
elif n>=60:
    print("Grade D")
elif n>=40:
    print("Grade E")
else:
    print("Grade F")