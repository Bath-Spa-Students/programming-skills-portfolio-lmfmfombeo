#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 

#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    "Variable": "A container for storing data in a program.",
    "Function": "A reusable block of code that performs a specific task.",
    "Conditional Statement": "A statement that allows the program to make decisions based on conditions.",
    "Loop": "A control structure that repeats a block of code until a certain condition is met.",
    "List": "A collection of items that can be of different data types and is ordered and mutable."}

glossary["Dictionary"] = "A collection of key-value pairs that are unordered and mutable."
glossary["Tuple"] = "An ordered and immutable collection of items."
glossary["String"] = "A sequence of characters, represented within single or double quotes."
glossary["Module"] = "A file containing Python code that can be imported and used in other programs."
glossary["Exception"] = "An event that occurs during the execution of a program that disrupts the normal flow of instructions."

# Printing each word and its meaning using a loop
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
