def find_most_frequent(elements):
    # Check if list is empty
    if not elements:
        return "Error: List cannot be empty"
    
    # Create a dictionary to store frequency counts
    frequency = {}
    
    # Count occurrences of each element
    for item in elements:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    # Find the element with the maximum frequency
    max_count = 0
    most_frequent = None
    
    for item, count in frequency.items():
        if count > max_count:
            max_count = count
            most_frequent = item
    
    return most_frequent

# Input a list of elements from the user
print("Input a list of elements to find the most frequent one:")
while True:
    user_input = input("Enter elements separated by spaces (e.g., 1 2 2 3 or a b a c): ").strip()
    
    # Check for empty or whitespace-only input
    if not user_input:
        print("Error: Input cannot be empty or just spaces. Please try again.")
        continue
    
    # Split input into a list
    elements = user_input.split()
    
    # Check if all elements are valid (not just spaces or empty strings)
    if not elements or all(el == "" for el in elements):
        print("Error: Invalid input format. Please enter meaningful elements separated by spaces.")
        continue
    
    # If we reach here, input is valid
    break

# Find and output the most frequent element
result = find_most_frequent(elements)
print(f"\nList: {elements}")
if isinstance(result, str) and result.startswith("Error"):
    print(result)  # Print error message if returned
else:
    print(f"Most Frequent Element: {result}")