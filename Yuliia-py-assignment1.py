#Canadian Business College. 
# Python Fundamentals  Assignment 1





#PART 1:-------------------------------


#enter how many courses did he/she finish
# the input value (which is string) is converted into number with int()

num_of_courses = int(input("How many courses have you finished? "))

print(num_of_courses)

#Declare an empty list
course_marks = []

#while loop
count = 1
while count <= num_of_courses:

# the append() method used to add user's input into    course_marks = []
course_marks.append (int(input("Enter your MARK for the COURSE #{count} is: ")))

#increment the loop count
count += 1	

print(course_marks)






#PART 2:-------------------------


#find the total of all the courses marks inside the list with loop
total = 0

for number in course_marks :
	  total += number



# find the average for all the courses

for numb in course_marks :

    average = total / num_of_courses

print(f"The average of your {num_of_courses} is:  {average}"))



#PART 3:------------------------

if average >= 90 and average <=100:
  print("your grade is A+")

if average >= 80 and average <=89:
  print("your grade is B")

if average >= 70 and average <=79:
  print("your grade is  C")

if average >= 60 and average <=69:
  print("your grade is D")

if average < 60: 
  print("your grade is F")
