#Write a python program that takes courses marks as input and then calculates average of all the
#courses. After calculating the average, calculate the percentage of a student using total marks. Assume
#the total of all the courses marks is 500 or take the total marks from the user as input. 

courses = int(input("Enter the number of courses: "))
course_marks = []

for i in range(courses):
    mark = float(input(f"Enter the marks for Course {i + 1}: "))
    course_marks.append(mark)

total_marks = 500

average = sum(course_marks) / len(course_marks)

percentage = (sum(course_marks) / total_marks) * 100

print(f"Average Course Mark: {average}")
print(f"Percentage: {percentage}%")
