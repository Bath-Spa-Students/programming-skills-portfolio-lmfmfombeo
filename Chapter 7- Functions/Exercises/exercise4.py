#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a
#medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size="large", message="love Python"):
    print(f"Creating a {size} shirt with the message: '{message}'")
make_shirt(size="medium")
make_shirt(size="small", message="Python")

