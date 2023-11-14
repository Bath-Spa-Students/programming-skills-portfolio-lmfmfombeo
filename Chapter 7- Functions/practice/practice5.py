# Write a Python program that defines a function to check whether a given no is prime.

def is_prime(no):
    if no <= 1:
        return False
    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            return False
    return True
input = int(input("Enter a no to check if prime: "))
if is_prime(input):
    print(f"{input} is a prime no.")
else:
    print(f"{input} is not prime no.")
