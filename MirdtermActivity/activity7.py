# Ryan Francis Camcaho Romano
# Bachelor of Science in Computer Science - Third Year - Block B
# Programming Language 101 - Tu.Th 08:30 AM-10:00 AM ABa 101
# Instructor: Mr. Ian Godwin Agapito
# Activity 7 - Midterm Activity
# (Individual): Import NumPy and the math module, then:
# Generate an array of 10 random numbers.
# Apply mathematical operations (square root, logarithm, exponential) to each value.

import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class ArrayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Array Math Operations")

        # Window setup
        window_width = 600
        window_height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Header
        tk.Label(root, text="Welcome!", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(root, text="Generate an array of 10 random numbers and apply mathematical operations", 
                font=("Arial", 10)).pack()

        # Option frame
        self.option_frame = ttk.Frame(root)
        self.option_frame.pack(pady=10)

        # Button styling
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 12), padding=10, background="#4CAF50", foreground="black")
        style.map("Custom.TButton", background=[("active", "#45a049")])

        # Buttons
        ttk.Button(self.option_frame, text="Random 10 Array", style="Custom.TButton", 
                  command=self.generate_random_array, width=25).pack(pady=5)  
        ttk.Button(self.option_frame, text="Input Array", style="Custom.TButton", 
                  command=self.input_array_loop, width=25).pack(pady=5)

        # Output area
        self.output = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD, font=("Arial", 12))
        self.output.pack(pady=10, fill=tk.BOTH, expand=True)

        # Footer
        footer_frame = ttk.Frame(root)
        footer_frame.pack(side=tk.BOTTOM, pady=10, fill=tk.X)
        tk.Label(footer_frame, text="PL 101 - Midterm Activity 7", 
                font=("Arial", 10, "italic")).pack()

    def clear_output(self):
        self.output.delete(1.0, tk.END)

    def display_array(self, array, include_math=True):
        self.clear_output()
        self.output.insert(tk.END, "Original Array (10 elements):\n")
        self.output.insert(tk.END, f"{np.round(array, 2)}\n\n")
        
        if include_math:
            # Apply mathematical operations
            sqrt_array = np.sqrt(array)
            log_array = np.log(array + 1e-10)  # Add small constant to avoid log(0)
            exp_array = np.exp(array)
            
            self.output.insert(tk.END, "Square Root:\n")
            self.output.insert(tk.END, f"{np.round(sqrt_array, 2)}\n\n")
            self.output.insert(tk.END, "Natural Logarithm:\n")
            self.output.insert(tk.END, f"{np.round(log_array, 2)}\n\n")
            self.output.insert(tk.END, "Exponential:\n")
            self.output.insert(tk.END, f"{np.round(exp_array, 2)}\n\n")
            
            # Detailed Results
            self.output.insert(tk.END, "Detailed Results:\n")
            for i in range(len(array)):
                self.output.insert(tk.END, f"Element {i+1}: {array[i]:.2f}\n")
                self.output.insert(tk.END, f"  √x = {sqrt_array[i]:.2f}\n")
                self.output.insert(tk.END, f"  ln(x) = {log_array[i]:.2f}\n")
                self.output.insert(tk.END, f"  e^x = {exp_array[i]:.2e}\n\n")
        
        # Array properties
        self.output.insert(tk.END, "Array Properties:\n")
        shape_str = f"(1, {array.shape[0]})" if len(array.shape) == 1 else str(array.shape)
        self.output.insert(tk.END, f"Shape: {shape_str}\n")
        self.output.insert(tk.END, f"Data Type: {array.dtype}\n")
        self.output.insert(tk.END, f"Size: {array.size}\n")

    def center_window(self, win, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        win.geometry(f"{width}x{height}+{x}+{y}")
    
    def generate_random_array(self):
        # Generate exactly 10 random numbers and apply math operations
        array = np.random.uniform(0, 100, 10)
        self.display_array(array)

    def input_array_loop(self):
        # Create a single dialog for input
        win = tk.Toplevel(self.root)
        win.title("Input Array")
        self.center_window(win, 500, 200)
        win.transient(self.root)
        win.grab_set()

        tk.Label(win, text="Enter numeric values separated by spaces (or 'x' to exit):", 
                font=("Arial", 10)).pack(pady=10)
        
        entry = ttk.Entry(win, width=50)
        entry.pack(pady=5)
        entry.focus_set()

        def process():
            input_str = entry.get().strip().lower()
            if input_str == 'x':
                win.destroy()
                return
            
            try:
                values = [float(x) for x in input_str.split()]
                array = np.array(values)
                win.destroy()  # Close the window first
                self.display_array(array)  # Then process the array
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric values or 'x' to exit")

        ttk.Button(win, text="Process", command=process).pack(pady=5)
        ttk.Button(win, text="Cancel", command=win.destroy).pack(pady=5)
        
        # Handle Enter key
        win.bind('<Return>', lambda event: process())

if __name__ == "__main__":
    root = tk.Tk()
    app = ArrayApp(root)
    root.mainloop()