#homogenous list / python supports hetrogenous list other than c , java

name =["mohd","bathspa","coding"]
print(name)

#hetrogenous
student = ["mohd","bathspa","year1","cc"]
print(student)

#Repetition operator * to repeat data
number = [1,2,3,4]
new_number = number * 2
print(new_number)

#index 
no = [10,20,30,40,50,60]
print(no[4])

#negative number 
no=[1,2,3,4,5,6,7,8,]
print(no[-5])

#The len function
number = [4,5,3,2,7,8,9,2,1]
print("number of element in a list :",len(number))

#mutability (changable)
number = [3,4,5,6,1,2,8]
number[0]=1
number[1]=2
print(number)

#Concatenating Lists
list1 =[2,3,4,5]
list2 =[6,7,8,9]
list3= list1+list2
print(list3)

#list slicing
new_list =[10,20,30,4,5,6,7]
result= new_list [2:4]
print(result)