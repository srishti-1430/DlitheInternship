#arithmetic operation
a=int(input("age of father: "))
b=int(input("age of sun: "))
print("addition of both father and sun age is : ",(a+b))
print("div :" ,(a/b))
print("sub :" ,(a-b))
print("mul :" ,(a*b))
print("mod :" ,(a%b))
print("floor:",(a//b))
print("exp:",(a**b))

a=int(input("enter a number "))
b=int(input("enter another number"))
print("reminder of these two numbers are ",(a%b))

#area of triangle
a=int(input("enter length :"))
b=int(input("enter width :"))
print("Area of rectangle is :",(a*b))

a=10
b=10
if (a==b):
    print("a is equal to b")

a=10
b=10
if (a!=b):
    print("a is not equal to b")
else:
    print("a and b are equal")

a=10
b=6
if (a!=b):
    a+=b
    print(a)

print(a==b)

a=10
b=6
if (a!=b):
    a-=b
    print(a)
    
a=10
b=6
if (a!=b):
    a*=b
    print(a)

a=int(input("enter your age :"))
if (a>=18):
    print("you are eligible to drive car ")
else:
    print("you are not eligible to drive  car")

#even or odd
a=int(input("enter an number :"))
b=a%2
if (b==0):
    print("Given number is even")
else:
    print("given digit is odd")

a=int(input("enter an number :"))
if (a%2==0):
    print("Given number is even")
else:
    print("given digit is odd")


a=int(input("enter mark of a student :"))
if (a>=80):
      print("student passed in examination")
elif (a>=75):
    print(" student is failed, but is eligible for re-examination")
else:
    print("student successfully failed in exam and also not eligible for re-exam ")
    
a=int(input("enter obtained mark :"))
b=int(input("enter total mark :"))
r=(a/b)*100
print("perecentage is :",r) 
if (a>=90):
    print("grade A")
elif(a>=80):
    print("garde B")
elif(a>=70):
    print("Grade c")
elif(a>=60):
    print("Grade D")
elif(a>=50):
    print("Grade E")
else:
    print("fail")

a=int(input("enter marks in maths :"))
b=int(input("enter marks in scince :"))
c=int(input("enter marks in history :"))
if(a<=80 or b<=80 or c<=80):
    print("fail")
else:
    print("pass")

a=int(input("sales of A :"))
b=int(input("sales of B :"))
c=int(input("sales of C :"))
if (a>=b and a>=c):
    print("Company A have highest sales")
elif (b>=a and a>=c):
    print("Company B have highest sales")
else:
    print("Company C have highest sales")


###task 1

s=int(input("enter new sales stat :"))
if (s>=90000):
    print("sales are good ")
elif(s>=70000 or s>=60000):
    print("sales are moderate")
elif(s<=60000):
    print("you are not eligible for continuing sales")
