#student_record_using_class-You are creating a system for a school to manage student records. Each student has:
#A name
#An age
#A grade
#A roll number
#Instead of writing separate variables for each student, you decide to create a class called Student to represent the blueprint for any student.
#By using a class, you can create multiple student records quickly and manage them efficiently.
#Objective Define a class called Student.
#Use attributes (name, age, grade, roll number).
#Create multiple student objects.
#Display each student’s information using a method.


# Define the Student class
class Student:
    def __init__(self, name, age, grade, roll_number):
        self.name = name
        self.age = age
        self.grade = grade
        self.roll_number = roll_number

    # Method to display student info
    def display_info(self):
        print("---- Student Record ----")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Grade       : {self.grade}")
        print(f"Roll Number : {self.roll_number}")
        print("------------------------")


# Creating multiple student objects
student1 = Student("Sneha", 14, "8th", 101)
student2 = Student("Amit", 15, "9th", 102)
student3 = Student("Riya", 13, "7th", 103)

# Displaying information for each student
student1.display_info()
student2.display_info()
student3.display_info()