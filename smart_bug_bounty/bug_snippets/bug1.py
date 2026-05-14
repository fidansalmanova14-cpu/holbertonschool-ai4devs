def get_last_elements(items, n):
    # Səhv: n=2 olduqda son iki elementi deyil, səhv hissəni qaytarır
    return items[len(items)-n+1:]

print(get_last_elements([1, 2, 3, 4, 5], 2)) 
