import tkinter as tk
from tkinter import messagebox

def find_most_frequent(elements):
    if not elements:
        return "Error: List cannot be empty"
    
    frequency = {}
    for item in elements:
        frequency[item] = frequency.get(item, 0) + 1
    
    max_count = 0
    most_frequent = None
    for item, count in frequency.items():
        if count > max_count:
            max_count = count
            most_frequent = item
    
    return most_frequent

def submit():
    # Get non-empty elements from entries
    elements = [entry.get().strip() for entry in entries if entry.get().strip()]
    if not elements:
        messagebox.showerror("Invalid Input", "Please enter at least one element.")
        return
    
    result = find_most_frequent(elements)
    if isinstance(result, str) and result.startswith("Error"):
        result_label.config(text=result, font=("Arial", 12, "bold"))
    else:
        result_label.config(text=f"Most Frequent: {result}", font=("Arial", 12, "bold"))

# Create the main window
root = tk.Tk()
root.title("Most Frequent Element Finder")
root.geometry("350x300")
root.resizable(False, False)

# Header label
tk.Label(root, text="Enter Elements (up to 5)", font=("Arial", 14)).pack(pady=10)

# Entry fields
entries = []
for i in range(5):
    e = tk.Entry(root, font=("Arial", 10), justify='center')
    e.pack(pady=4)
    entries.append(e)

# Submit button
submit_btn = tk.Button(root, text="Find Most Frequent", command=submit)
submit_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Footer label
tk.Label(root, text="PL101 - Midterm Exam Question 16-25", font=("Arial", 9, "italic")).pack(side=tk.BOTTOM, pady=5)

# Start the application
root.mainloop()