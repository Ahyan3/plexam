def find_second_largest(numbers):
    # Check if list has fewer than 2 elements (though we’ll enforce 5 inputs)
    if len(numbers) < 2:
        return "List must have at least two numbers"
     
    # Initialize largest and second largest
    largest = None
    second_largest = None
    
    # Single pass through the list
    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif (second_largest is None or num > second_largest) and num != largest:
            second_largest = num
    
    # Handle case where no second largest exists
    if second_largest is None:
        return "No second largest number exists (all numbers might be the same)"
    
    return second_largest

# Input five numbers individually
print("Input a list of 5 numbers to find the second largest number:")
numbers = []

# Collect 5 inputs with error handling
for i in range(1, 6):
    while True:
        try:
            num = float(input(f"Input number {i}: "))
            numbers.append(num)
            break
        except ValueError: 
            print("Invalid input! Please enter a valid number.")

# Find and output the second largest number
result = find_second_largest(numbers)
print(f"\nList: {numbers}")
print(f"Second Largest Number: \033[1m{result}\033[0m") 