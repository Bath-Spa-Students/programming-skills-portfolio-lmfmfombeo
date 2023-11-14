# Write a Python program that uses a function to check if a given number is prime or not

def is_prime (no):
    if no <= 1:
        return False
    for i in range (2, int(no ** 0.5)+1):
        if no % i == 0:
            return False
        return True
input = int(input("enter the no if its prime: "))
if is_prime(input):
    print(f"{input} is prime no.")
else:
    print(f"{input} is not prime no.")    
 