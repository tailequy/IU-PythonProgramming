students = {"Emily": 22, "David": 19}
def print_student_age():
   while True:
       try:
           name = input("Enter name of student: ")
           print(students[name])
           break
       except:
           print("Name not registered")
       finally:
           print("…terminating")
print_student_age()
