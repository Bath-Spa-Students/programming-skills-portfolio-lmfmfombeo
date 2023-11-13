#Write a python program that takes an input 5 from user and then type cast those values to string, int
#and float in the separate variables. Print all the variables.

value1 = input("Enter a value: ")
value2 = input("Enter a value: ")
value3 = input("Enter a value: ")
value4 = input("Enter a value: ")
value5 = input("Enter a value: ")


str1 = str(value1)
str2 = str(value2)
str3 = str(value3)
str4 = str(value4)
str5 = str(value5)
           
int1 = int(value1)
int2 = int(value2)
int3 = int(value3)
int4 = int(value4)
int5 = int(value5)


float1 = float(value1)
float2 = float(value2)
float3 = float(value3)
float4 = float(value4)
float5 = float(value5)

# Print all variables
print("String values:", str1, str2, str3, str4, str5)
print("Integer values:", int1, int2, int3, int4, int5)
print("Float values:", float1, float2, float3, float4, float5)
