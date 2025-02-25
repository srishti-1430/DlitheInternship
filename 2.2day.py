#check if the list is sorted or not
def is_sorted(lst):
    return lst == sorted(lst)
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
if is_sorted(numbers):
    print("The list is sorted.")
else:
    print("The list is not sorted.")

#Convert Binary to Decimal
def binary_to_decimal(binary_str):
    return int(binary_str, 2)
binary = input("Enter a binary number: ")
if all(bit in '01' for bit in binary):
    decimal = binary_to_decimal(binary)
    print(f"Decimal equivalent: {decimal}")
else:
    print("Invalid binary number. Please enter only 0s and 1s.")

#Convert Decimal to Binary
def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:] 
decimal = int(input("Enter a decimal number: "))
binary = decimal_to_binary(decimal)
print(f"Binary equivalent: {binary}")

#Tribonacci sequence
def tribonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    tribo = [0, 1, 1]
    
    for i in range(3, n):
        tribo.append(tribo[i-1] + tribo[i-2] + tribo[i-3])
    return tribo
num_terms = int(input("Enter the number of terms: "))
print("Tribonacci sequence:", tribonacci(num_terms))

#sum of numbers
try:
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    if numbers:
        print("Sum of the numbers:", sum(numbers))
    else:
        print("Error: Please enter at least one number.")
except ValueError:
    print("Error: Please enter only numeric values.")


#producto of numbers
import math
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
product = math.prod(numbers) 
print("Product of the numbers:", product)

#pattern 
def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

n = int(input("Enter the number of rows: "))
print_pyramid(n)

#PATTERN 2
def print_square(n):
    for i in range(n):
        print("* " * n)
n = int(input("Enter the number of rows and columns: "))
print_square(n)




