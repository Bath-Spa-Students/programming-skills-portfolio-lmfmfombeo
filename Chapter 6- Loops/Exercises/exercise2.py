#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

#they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 

#age, and then tell them the cost of their movie ticket

while True:
    try:
        age = int(input("Please enter your age (or type 'quit' to exit): "))
    except ValueError:
        print("Invalid input. Please enter a valid age or 'quit' to exit.")
        continue

    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    print(f"The cost of your movie ticket is ${ticket_price}")

    if age >= 3:
        another = input("Do you want to check another ticket price? (yes/no): ")
        if another.lower() != 'yes':
            break
    else:
        print("Enjoy your free ticket!")

print("Thank you for using our ticket pricing service!")

