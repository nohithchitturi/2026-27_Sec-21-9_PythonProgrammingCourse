# Example solution: remove duplicates from a list
list_data = [1, 2, 2, 3, 1, 4, 3]
unique = []
for item in list_data:
    if item not in unique:
        unique.append(item)
print("Original:", list_data)
print("Without duplicates:", unique)