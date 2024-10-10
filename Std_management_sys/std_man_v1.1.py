class Std:
  def __init__(self, name, rollno, course, cgpa):
    self.name = name
    self.rollno = rollno
    self.course = course
    self.cgpa = cgpa
  
  def __str__(self):
    return f"Name: {self.name}\n,Roll No: {self.rollno}\nCourse: {self.course}\nCGPA: {self.cgpa}"
  
std_list = []

def enter_std_date():

  while(True):
    print("\n(1)Enter new Student\n(2)Display by rollno\n(3)Display All\n(4)Delete by rollno\n(5)Delete all")
    print("===================================================")
    user_input = input("Enter Command:")
    print("===================================================")

    match user_input:
      case "1":
        enter_data()
      case "2":
        display_sep()
      case "3":
        display_all()
      case "5":
        delete_all()
      case "4":
        delete_spe()

def enter_data():
  global std_list
  while(True):
    
    name = input("Enter student name: ")
    rollno = input("Enter student rollno: ")
    course = input("Enter student course: ")
    cgpa = input("Enter student cgpa: ")

    std_obj = Std(name, rollno, course, cgpa)
    std_list.append(std_obj)
    print("-------------------------------------")
    more = input("Enter more (yes/no)?: ").lower()
    print("-------------------------------------")

    if more == "no":
      return
    
def delete_all():
  global std_list
  std_list.clear()
  return

def delete_spe():
  while(True):
    
    delete_rollno = input("Enter the roll number of the target student: ")
    student_found= False
    for std_obj in std_list:
      if std_obj.rollno == delete_rollno:
        std_list.remove(std_obj)
        print(f"Student with Rollno : {delete_rollno} has been removed")
        student_found = True
    if not student_found:
      print(f"Student with Roll No: {delete_rollno} not found")
    print("-------------------------------------")
    more = input("Continue Operation (yes/no)?: ").lower()
    print("-------------------------------------")
    if more == "no":
      return
    
    
def display_all():
  global std_list
  if not std_list:
    print("No Student to Display!")
  else:
    for std in std_list:
      print(f"Name: {std.name}, Roll No: {std.rollno}, Course: {std.course}, CGPA: {std.cgpa}")

def display_sep():
  while(True):
    rollno = input("Enter the roll number to display: ")
    global std_list
    found = False

    for std in std_list:
      if std.rollno == rollno:
        print(f"Name: {std.name}, Roll No: {std.rollno}, Course: {std.course}, CGPA: {std.cgpa}")
        found = True
        break
    if not found:
      print(f"No Student found with roll number {rollno}")
    print("-------------------------------------")
    more = input("Continue Operation (yes/no)?: ").lower()
    print("-------------------------------------")
    if more == "no":
      return
    
enter_std_date()

    