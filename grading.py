print("Enter your marks")
a=int(input())
b=int(input())
c=int(input())
d=int(input()) 
e=int(input())
sum=a+b+c+d+e
print(sum)
avg= sum/5
print(sum/5)

if avg >=70 and avg<=100:
       print("Your grade is A") 
elif avg >=60 and avg<69:
    print("Your grade is B")
elif avg >=50 and avg<59:
    print("Your grade is C")
elif avg >=40 and avg<49:
    print("Your grade is D")
elif avg >=30 and avg<39:
    print("FAIL")


