original_set = {1, 2, 3, 4, 5}
alias_of_set = original_set
alias_of_set.add(0)
print("Initial Set:", original_set)
print("Alias of Set:", alias_of_set)

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Dictionary to store student names and their grades
students = {}

# Function to add a new student
def add_student(name):
    if name not in students:
        students[name] = []
        return f"Student {name} has been added."
    else:
        return f"Student {name} already exists."

# Function to add a grade for an existing student
def add_student_grade(name, grade):
    if name in students:
        students[name].append(grade)
        return f"Grade {grade} has been added for student {name}."
    else:
        return f"Student {name} doesn't exist."

# Function to print all grades for a specific student
def print_grades(name):
    if name not in students:
        return f"Student {name} doesn't exist."
    else:
        return f"All grades for {name}: {students[name]}"
    

global_var = 9

def func():
    local_var = 5
    print("Inside the function:")
    print("Local variable:", local_var)  
    print("Global variable:", global_var)  

print("Outside the function:")
print("Global variable:", global_var)  

func()

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_students(self):
        while True:
            name = input("Please enter the student's name (type 'done' to finish): ")
            if name.lower() == 'done':
                break
            self.students[name] = None

    def input_grades(self):
        for student in self.students:
            while True:
                try:
                    grade = float(input(f"Please enter the grade for {student}: "))
                    self.students[student] = grade
                    break
                except ValueError:
                    print("Invalid input, please enter a valid float number.")

    def get_grade(self):
        name = input("Please enter the student's name: ")
        if name in self.students:
            grade = self.students[name]
            if grade is None:
                print(f"The grade for {name} has not been entered yet.")
            else:
                print(f"The grade for {name} is: {grade}")
        else:
            print("No record")

    def menu(self):
        while True:
            choice = input("Please choose an action (Add, Grades, Get, Exit): ").strip().lower()
            if choice == 'add':
                self.add_students()
            elif choice == 'grades':
                self.input_grades()
            elif choice == 'get':
                self.get_grade()
            elif choice == 'exit':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice, please try again.")

# Create a StudentManager object and call the menu method
if __name__ == "__main__":
    manager = StudentManager()
    manager.menu()
