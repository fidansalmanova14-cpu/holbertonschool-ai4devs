"""
Task: Return the last n items in a list.
Intended Behavior: 
If n=2 and list=[1,2,3,4,5], it should return [4, 5].
"""

def get_last_elements(items, n):
    # This logic has an off-by-one error
    # It starts the slice one position too late
    if n <= 0:
        return []
    
    # Buggy line:
    return items[len(items) - n + 1:]

# Example usage for testing
my_list = [10, 20, 30, 40, 50, 60]
requested_n = 3
result = get_last_elements(my_list, requested_n)

print(f"List: {my_list}")
print(f"Requested last {requested_n} elements.")
print(f"Result: {result}") # Should be [40, 50, 60]
