#Write a Python program that uses a while loop to find the largest number among a series of
#user-input values until they enter '0' to exit the loop.

largest = float("inf")

while True:
    no = float(input("enter number (enter 0 to exit): "))

    if no == 0: 
        break
    largest = max(largest,no)

if largest == float("inf"):
    print("no valid no added.")  
else: 
    print("largest no entered is:", largest )      