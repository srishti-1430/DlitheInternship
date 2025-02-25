#sum of two numbers
a=int(input("enter a number: "))
b=int(input("enter another number: "))
print(a+b)

#sum of three numbers
a=int(input("enter a number: "))
b=int(input("enter another number: "))
c=int(input("enter one more number: "))
print(a+b+c)

#check odd or even
a=int(input("enter a number to check odd or even :"))
if a%2==0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")

#find factorial of number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
a=int(input("enter a number :"))
print(f"Factorial of {a} is {factorial(a)}")

# largest number of three number
a=int(input("enter a number: "))
b=int(input("enter another number: "))
c=int(input("enter one more number: "))
d=max(a,b,c)
print(f"largest number is {d}")

# check palindrome
a=input("enter anything to check palindrome :")
if a==a[::-1]:
    print(f"{a} is palindrome")
else:
    print(f"{a} is not plaindrome")

#fibboncci series
n = int(input("Enter the number of terms: "))
a, b = 0, 1

print("Fibonacci Series:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
    
#count vowels
a = input("Enter a string: ").lower()
vowels = "aeiou"
vc = 0
for char in a:
    if char in vowels:
        vc += 1
print(f"Number of vowels: {vc}")

#count consonents
a = input("Enter a string: ").lower()
vowels = "aeiou"
cc = 0
for char in a:
    if char not in vowels:
        cc += 1
print(f"Number of consonents: {cc}")

#prime number
a = int(input("Enter a number: "))

if a > 1 and all(a% i != 0 for i in range(2, a)):
    print(f"{a} is a prime number.")
else:
    print(f"{a} is not a prime number.")

#multiplication table
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

#tuple
v=("hello","wow")
y=list(v)
y[1]="hii"
v=tuple(y)
print(v)

v=("hello","wow")
y=list(v)
y.append("ssss")
v=tuple(y)
print(v)

v=("hello","wow")
y=list(v)
y.remove("wow")
v=tuple(y)
print(v)

v=("hello","wow")
y=list(v)
y.insert(2,"hiii")
v=tuple(y)
print(v)

ic=("chikku almond","vanilla")
ic2=("butterscoch","rosted almond")
a=list(ic)
b=list(ic2)
a.extend(b)
ic=tuple(a)
ic2=tuple(b)
print(ic)

v=("hello","wow")
y=list(v)
y.pop(1)
v=tuple(y)
print(v)

cities=("udupi","manglore","banglore")
a=list(cities)
a[2]="hebri"
cities=tuple(a)
print(cities)
