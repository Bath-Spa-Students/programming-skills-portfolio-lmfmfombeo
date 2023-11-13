#Write a Python program that uses the break statement to exit a for loop when a specific
#condition is met.

for no in range(1, 11):
    if no == 7:
        print("Exiting loop.")
        break
    print(no)
