import tkinter as tk
from tkinter import messagebox

def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least two numbers"

    largest = None
    second_largest = None

    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif (second_largest is None or num > second_largest) and num != largest:
            second_largest = num

    if second_largest is None:
        return "No second largest number (all numbers may be the same)"
    return second_largest

def submit():
    try:
        nums = [float(entry.get()) for entry in entries]
        result = find_second_largest(nums)
        result_label.config(text=f"Second Largest: {result}", font=("Arial", 12, "bold"))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers only.")

root = tk.Tk()
root.title("Second Largest Finder")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Enter 5 Numbers", font=("Arial", 14)).pack(pady=10)

entries = []
for i in range(5):
    e = tk.Entry(root, font=("Arial", 10), justify='center')
    e.pack(pady=4)
    entries.append(e)

submit_btn = tk.Button(root, text="Find Second Largest", command=submit)
submit_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

tk.Label(root, text="PL 101 Midterm Exam Question 11-15", font=("Arial", 9, "italic")).pack(side=tk.BOTTOM, pady=5)

root.mainloop()