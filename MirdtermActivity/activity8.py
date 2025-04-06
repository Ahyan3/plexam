# Ryan Francis Camcaho Romano
# Bachelor of Science in Computer Science - Third Year - Block B
# Programming Language 101 - Tu.Th 08:30 AM-10:00 AM ABa 101
# Instructor: Mr. Ian Godwin Agapito
# Activity 8 - Midterm Activity
# (Pair Work): Write a custom Python module containing two NumPy functions and import it into another script. 



import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import numpy as np
from numpy_operations import create_array, calculate_statistics # Importing custom module named numpy_operations.py

class ArrayAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Array Analyzer")

        # Window configuration
        window_width, window_height = 600, 650
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        tk.Label(root, text="Welcome!", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(root, text="Process arrays using custom NumPy functions", 
                font=("Arial", 10)).pack()

        # Button frame
        self.option_frame = ttk.Frame(root)
        self.option_frame.pack(pady=10)
        
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 12), padding=10)
        
        ttk.Button(self.option_frame, text="Generate Random Array", style="Custom.TButton",
                  command=self.generate_array, width=25).pack(pady=5)
        ttk.Button(self.option_frame, text="Enter Custom Array", style="Custom.TButton",
                  command=self.custom_array, width=25).pack(pady=5)

        # Results display
        self.results_text = scrolledtext.ScrolledText(main_frame, 
                                                    width=50, 
                                                    height=20,
                                                    font=("Courier", 10))
        self.results_text.pack(pady=10, fill=tk.BOTH, expand=True)

        # Footer
        footer_frame = ttk.Frame(root)
        footer_frame.pack(side=tk.BOTTOM, pady=6, fill=tk.X)
        ttk.Label(footer_frame, text="PL 101 - Midterm Activity 8(Pair work)", 
                 font=("Helvetica", 10, "italic")).pack()

    def display_results(self, array):
        """Display array and its statistics"""
        stats = calculate_statistics(array)
        self.results_text.delete(1.0, tk.END)
        
        self.results_text.insert(tk.END, "Generated Array:\n")
        self.results_text.insert(tk.END, f"{np.round(array, 2)}\n\n")
        
        self.results_text.insert(tk.END, "Statistical Analysis:\n")
        self.results_text.insert(tk.END, f"Mean: {stats['mean']:.2f}\n")
        self.results_text.insert(tk.END, f"Std Dev: {stats['std']:.2f}\n")
        self.results_text.insert(tk.END, f"Minimum: {stats['min']:.2f}\n")
        self.results_text.insert(tk.END, f"Maximum: {stats['max']:.2f}\n")
        self.results_text.insert(tk.END, f"Median: {stats['median']:.2f}\n")

    def generate_array(self):
        """Generate and display random array"""
        array = create_array()  # Using module function
        self.display_results(array)

    def custom_array(self):
        """Create dialog for custom array input"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Custom Array")
        dialog.geometry("300x150")
        dialog.transient(self.root)
        dialog.grab_set()

        ttk.Label(dialog, text="Enter numbers (space-separated):").pack(pady=10)
        
        entry = ttk.Entry(dialog, width=30)
        entry.pack(pady=5)
        entry.focus()

        def process():
            try:
                numbers = [float(n) for n in entry.get().split()]
                array = np.array(numbers)
                dialog.destroy()
                self.display_results(array)
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")

        ttk.Button(dialog, text="Analyze", command=process).pack(pady=10)
        
        # Bind Enter key
        dialog.bind('<Return>', lambda e: process())

if __name__ == "__main__":
    root = tk.Tk()
    app = ArrayAnalyzer(root)
    root.mainloop()