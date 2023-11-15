#Write a Python program to iterate through both the keys and values of a dictionary and print them

dict = {'a':"cat",'b':"bat",'c':"dog"}
for key, value in dict.items():
    print(f"key: {key}, value: {value}")