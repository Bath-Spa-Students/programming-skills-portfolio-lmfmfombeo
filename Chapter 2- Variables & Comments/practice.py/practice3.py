#Write a python program that takes an input 5 from user and then type cast those values to string, int
#and float in the separate variables. Print all the variables.

#five values 
value1 = input("Enter a value: ")
value2 = input("Enter a value: ")
value3 = input("Enter a value: ")
value4 = input("Enter a value: ")
value5 = input("Enter a value: ")

#string
str_value1 = str(value1)
str_value2 = str(value2)
str_value3 = str(value3)
str_value4 = str(value4)
str_value5 = str(value5)

#int
int_value1 = int(value1)
int_value2 = int(value2)
int_value3 = int(value3)
int_value4 = int(value4)
int_value5 = int(value5)

#float
float_value1 = float(value1)
float_value2 = float(value2)
float_value3 = float(value3)
float_value4 = float(value4)
float_value5 = float(value5)

# Print all variables
print("String values:", str_value1, str_value2, str_value3, str_value4, str_value5)
print("Integer values:", int_value1, int_value2, int_value3, int_value4, int_value5)
print("Float values:", float_value1, float_value2, float_value3, float_value4, float_value5)
