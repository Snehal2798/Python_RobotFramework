# 1. Define the Student class (The Blueprint)
class Student:
    def __init__(self, name, age, grade, roll_number):
        # Initializing attributes
        self.name = name
        self.age = age
        self.grade = grade
        self.roll_number = roll_number

    # 2. Method to display student information
    def display_info(self):
        print(f"Student Record: [Roll #{self.roll_number}]")
        print(f"Name: {self.name}")
        print(f"Age:  {self.age}")
        print(f"Grade: {self.grade}")
        print("-" * 30)

# 3. Create multiple student objects (Instances)
student1 = Student("Alice Johnson", 14, "9th", 101)
student2 = Student("Mark Smith", 15, "10th", 102)
student3 = Student("Chloe Davis", 14, "9th", 103)

# 4. Display each student's information
print("--- School Management System ---\n")
student1.display_info()
student2.display_info()
student3.display_info()