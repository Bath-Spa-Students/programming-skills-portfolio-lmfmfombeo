#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 
#each word-meaning pair in your output.

glossary = {"Variable": "A container for storing data in a program.",
    "Function": "A reusable block of code that performs a specific task.",
    "Conditional Statement": "A statement that allows the program to make decisions based on conditions.",
    "Loop": "A control structure that repeats a block of code until a certain condition is met.",
    "List": "A collection of items that can be of different data types and is ordered and mutable."}

for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
