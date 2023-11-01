#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet


pets = [{ "kind": "Dog","owner": "Ali"},{"kind": "Cat","owner": "ahmed" },{"kind": "Fish","owner": "mohd"},{"kind": "Parrot","owner": "bob"}]


for pet in pets:
    print(f"Pet Kind: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}")
    print()
