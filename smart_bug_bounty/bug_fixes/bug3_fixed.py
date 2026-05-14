"""
Task: Manage a list of students.
Fixed Version: Avoids mutable default arguments.
"""

def add_student(name, student_list=None):
    # Fixed: Default is None, list is initialized inside
    if student_list is None:
        student_list = []
    
    student_list.append(name)
    print(f"Added {name}. Current List: {student_list}")
    return student_list

# Verification calls
class_a = add_student("Alice")
class_a = add_student("Bob")
# This will now correctly start with an empty list
class_b = add_student("Charlie") 
