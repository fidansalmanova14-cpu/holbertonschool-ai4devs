def add_student(name, student_list=None):
    # Fixed: Using None as default and initializing list inside to avoid shared state
    if student_list is None:
        student_list = []
    
    student_list.append(name)
    return student_list

print("Class A:", add_student("Alice"))
print("Class B:", add_student("Charlie")) # Now correctly returns only ['Charlie']
