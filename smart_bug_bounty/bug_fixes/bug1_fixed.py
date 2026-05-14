"""
Task: Return the last n items in a list.
Fixed Version: Uses negative slicing for robustness.
"""

def get_last_elements(items, n):
    # Validation check for n
    if n <= 0:
        return []
    
    # Pythonic way to handle slicing from the end
    # items[-n:] correctly handles all cases even if n > len(items)
    return items[-n:]

def test_fix():
    test_data = [1, 2, 3, 4, 5]
    result = get_last_elements(test_data, 2)
    print(f"Input: {test_data}, n=2 -> Result: {result}")
    assert result == [4, 5]

if __name__ == "__main__":
    test_fix()
