def get_last_elements(items, n):
    if n <= 0:
        return []
    # Fixed: Simplified slicing to correctly get the last n elements
    return items[-n:]

# Quick test
print(get_last_elements([1, 2, 3, 4, 5], 2)) # Expected: [4, 5]
