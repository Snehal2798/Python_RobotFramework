#You are developing a program for a school competition where two students took a test. The school wants to know which student scored higher so they can announce the winner.
#Your task is to write a program that:
#Takes the scores of two students as input.
#Compares the scores using an if-else statement.
#Displays who scored higher or if it’s a tie.

print("**********************STUDENT COMPETITION***********************")
markofstudent1=float(input("Enter the student 1 marks:"))
markofstudent2=float(input("Enter the student 2 marks:"))
if markofstudent1>markofstudent2:
        print("Student 1 got highest score")
elif markofstudent2>markofstudent1 :
        print("Student 2 got highest score")
else:
    print("Both students have the same score")