# Write a Python program that defines a function to check whether a given no is prime.
def is_prime(no):
    if no <= 1:
        return False
    for i in range(2, int(no**0.5) + 1):
        if no % i == 0:
            return False
    return True
number = 17

if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
