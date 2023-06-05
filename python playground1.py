
# swap 2 nos
from typing import Any

a = 15
b = 25
print("before sawapping ")
print('a= ', a)
print('b=', b)
temp = a
a = b
b = temp
print("after sawapping ")
print('a= ', a)
print('b=', b)

# palindrome

def is_palindrome(number):
    original_number = number
    reversed_number = 0


    while number > 0:
        remainder = number % 10
        reversed_number = reversed_number * 10 + remainder
        number //= 10

    # Compare
    if original_number == reversed_number:
        return True
    else:
        return False

#  input
num = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")



