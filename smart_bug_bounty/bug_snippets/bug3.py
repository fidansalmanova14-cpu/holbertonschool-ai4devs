"""
Task: Manage a list of students in a class.
Intended Behavior:
Each call to add_student should create a fresh list if none provided.
"""

def add_student(name, student_list=[]):
    # Bug: Mutable default arguments are evaluated only once
    # This leads to shared state between different calls
    student_list.append(name)
    print(f"Current list state: {student_list}")
    return student_list

print("--- Class A ---")
class_a = add_student("Alice")
class_a = add_student("Bob")

print("\n--- Class B ---")
# Expected: ['Charlie'], Actual: ['Alice', 'Bob', 'Charlie']
class_b = add_student("Charlie")

print("\nExecution complete.")
