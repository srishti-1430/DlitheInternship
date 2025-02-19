age=20
if(age>18):
    print("eligible for voting")
else:
    print("not eligible for voting")

a="10"
b="hello"
print(a)
print(b)
s=a+b
print(s)

###casting
B='3'
b="a"
print(B)
print(b)

a=float(50)
print(a)
b=str(8.9)
print(b)
c=str(9)
print(c)

print(type(a))

#variables
on_1=4
print(on_1)

a,b,c=1,2,"sri"
print(a)
print(b)
print(c)

#assining same value for different variable
a=b=c=20
print(a)
print(b)
print(c)

fruits=["mango","chikku","orenge"]
x,y,z=fruits
print(x)
print(y)
print(z)

a="python"
b="is"
c="awesome"
print(a,b,c)

a=int(input("enter a num"))
b=int(input("enter a second num"))
print(a+b)
      
#swapping
x=2
y=7
x,y=y,x
print(x)
print(y)

#global variable
x=20
def myfunction():
    print(x)
myfunction()
