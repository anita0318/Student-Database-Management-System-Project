class StudentDatabase:
    __student_list =[] #private class attribute

    @classmethod
    def add_student(cls,student):
        cls.__student_list.append(student)
    @classmethod
    def get_students(cls):
        return cls.__student_list
    
    @classmethod
    def find_student(cls,student_id):
        for student in cls.__student_list:
            if student._Student__student_id ==student_id:
                return student
        else:
            return None 
        
class Student:
    def __init__(self,student_id,name,department):
        self.__student_id =student_id #private
        self.__name =name             #private
        self.__department =department #private
        self.__is_enrolled =False     #private, default false

        StudentDatabase.add_student(self) #auto insert into database

    
    def enroll_student(self):
        if self.__is_enrolled:
            print(f"{self.__name} is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f'{self.__name} has been successfully enrolled.')
    def drop_student(self):
        if not self.__is_enrolled:
            print(f'{self.__name} is not currently enrolled.')
        else:
            self.__is_enrolled = False
            print(f'{self.__name} has been dropped')

    def view_student_info(self):
        if self.__is_enrolled:
            status = "Enrolled"
        else:
            status ="Not Enrolled"
        print(" ")
        print(f" Studnet id : {self.__student_id}")
        print(f" Name       : {self.__name}")
        print(f" Department : {self.__department}")
        print(f" Status     : {status}")
        print(" ")
#task 3 manual input
s1 = Student("0001","Mita Ahmed","Computer Science")
s2 = Student("0002","Sazzad Hossain","Pharmacy")
s3 = Student("0003","Ritu Akter","Microbiology")

#task 7 Menu system
def menu():
    while True:
        print("\n")
        print("Student Management System")
        print("1.View All Students")
        print("2.Enroll Student")
        print("3.Drop Student")
        print("4.Exit")

        choice =input("Enter your choice (1-4): ")   
        if choice =="1":
            students =StudentDatabase.get_students()
            if not students:
                print("No students found.")
            else:
                for student in students:
                    student.view_student_info()

        elif choice =="2":
            s_id =input("Enter Student ID to enroll: ")
            student = StudentDatabase.find_student(s_id)
            if student is None:
                print(f"No student found with this ID '{s_id}'.")
            else:
                student.enroll_student()
        
        elif choice =="3":
            s_id =input("Enter Student ID to drop: ") 
            student = StudentDatabase.find_student(s_id)
            if student is None:
                print(f"No student found with this ID '{s_id}'.")
            else:
                student.drop_student()

        elif choice =="4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, Please enter a number between 1 to 4.")


menu()
