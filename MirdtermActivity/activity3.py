# Ryan Francis Camcaho Romano
# Bachelor of Science in Computer Science - Third Year - Block B
# Programming Language 101 - Tu.Th 08:30 AM-10:00 AM ABa 101
# Instructor: Mr. Ian Godwin Agapito
# Activity 3 - Midterm Activity
# (Individual) Generate a 5x5 random NumPy array and perform:
# Mean, median, and standard deviation calculations.
# Element-wise operations with another array.
# Reshaping the array into a different dimension.


import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class ArrayApp:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Array Creator")

        window_width = 600
        window_height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        tk.Label(root, text="Welcome!", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(root, text="Create arrays and view their properties.", font=("Arial", 10)).pack()

        self.option_frame = ttk.Frame(root)
        self.option_frame.pack(pady=10)

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 12), padding=10, background="#4CAF50", foreground="black")
        style.map("Custom.TButton", background=[("active", "#45a049")])

        ttk.Button(self.option_frame, text="Random Array", style="Custom.TButton", 
                  command=self.random_five_by_five, width=25).pack(pady=5)  
        ttk.Button(self.option_frame, text="Input Array", style="Custom.TButton", 
                  command=self.input_array, width=25).pack(pady=5)

        # Output area with expand=True to fill available space
        self.output = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD, font=("Arial", 12))
        self.output.pack(pady=10, fill=tk.BOTH, expand=True)

        # Footer
        footer_frame = ttk.Frame(root)
        footer_frame.pack(side=tk.BOTTOM, pady=10, fill=tk.X)
        tk.Label(footer_frame, text="PL 101 - Midterm Activity 3", font=("Arial", 10, "italic")).pack()

    def clear_output(self):
        self.output.delete(1.0, tk.END)

    def display_array(self, array):
        # Display the array and its properties, adjusting shape for 1D arrays
        self.clear_output()
        self.output.insert(tk.END, "Array created:\n")
        self.output.insert(tk.END, f"{array}\n\n")
        self.output.insert(tk.END, "Array Properties:\n")
        # For 1D arrays, convert shape (n,) to (1, n)
        if len(array.shape) == 1:
            shape_str = f"(1, {array.shape[0]})"
        else:
            shape_str = str(array.shape)
        self.output.insert(tk.END, f"Shape: {shape_str}\n")
        self.output.insert(tk.END, f"Data Type: {array.dtype}\n")
        self.output.insert(tk.END, f"Size: {array.size}\n")

    def center_window(self, win, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        win.geometry(f"{width}x{height}+{x}+{y}")

    def input_array(self):
        # Popup for choosing input type
        win = tk.Toplevel(self.root)
        win.title("Input Array")
        self.center_window(win, 500, 300)
        win.transient(self.root)
        win.grab_set()

        tk.Label(win, text="Choose input method:", font=("Arial", 10)).pack(pady=10)
        method = tk.StringVar(value="manual_1d")  
        ttk.Radiobutton(win, text="Manual Input (1D)", variable=method, value="manual_1d", 
                        command=lambda: self.show_manual_1d(win)).pack(pady=5)
        ttk.Radiobutton(win, text="Multi-dimensional", variable=method, value="multi_d", 
                        command=lambda: self.show_multi_dimensional(win)).pack(pady=5)

        # Frame to hold dynamic input fields
        self.input_frame = ttk.Frame(win)
        self.input_frame.pack(pady=10)
        self.show_manual_1d(win)  

    def show_manual_1d(self, parent):
        # Show input fields for Manual Input (1D)
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        tk.Label(self.input_frame, text="Enter values separated by spaces:", font=("Arial", 10)).pack()
        entry = ttk.Entry(self.input_frame, width=30)
        entry.pack(pady=5)

        def process():
            try:
                values = [float(x) for x in entry.get().split()]
                array = np.array(values)
                self.display_array(array)
                parent.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter numeric values only.")

        ttk.Button(self.input_frame, text="Create", command=process).pack(pady=5)
        ttk.Button(self.input_frame, text="Cancel", command=parent.destroy).pack(pady=5)

    def show_multi_dimensional(self, parent):
        # Show input fields for Multi-dimensional array
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        tk.Label(self.input_frame, text="Enter dimensions (e.g., '2 3'):", font=("Arial", 10)).pack()
        dims_entry = ttk.Entry(self.input_frame, width=30)
        dims_entry.pack(pady=5)
        tk.Label(self.input_frame, text="Enter values separated by spaces:", font=("Arial", 10)).pack()
        values_entry = ttk.Entry(self.input_frame, width=30)
        values_entry.pack(pady=5)

        def process():
            try:
                dim_list = [int(x) for x in dims_entry.get().split()]
                total_size = np.prod(dim_list)
                values = [float(x) for x in values_entry.get().split()]
                if len(values) != total_size:
                    messagebox.showerror("Error", f"Number of values ({len(values)}) must match size ({total_size})")
                    return
                array = np.array(values).reshape(dim_list)
                self.display_array(array)
                parent.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric values.")

        ttk.Button(self.input_frame, text="Create", command=process).pack(pady=5)
        ttk.Button(self.input_frame, text="Cancel", command=parent.destroy).pack(pady=5)

    def random_five_by_five(self):
        # Generate two 5x5 random arrays and perform operations (Activity 3)
        array1 = np.random.uniform(0, 10, (5, 5))  # First 5x5 array
        array2 = np.random.uniform(0, 10, (5, 5))  # Second 5x5 array for element-wise operation

        # Clear output and display first array
        self.clear_output()
        self.output.insert(tk.END, "First 5x5 Random Array:\n")
        self.output.insert(tk.END, f"{array1}\n\n")

        # Calculate and display statistics for first array
        self.output.insert(tk.END, "Statistics (First Array):\n")
        self.output.insert(tk.END, f"Mean: {np.mean(array1):.2f}\n")
        self.output.insert(tk.END, f"Median: {np.median(array1):.2f}\n")
        self.output.insert(tk.END, f"Standard Deviation: {np.std(array1):.2f}\n\n")

        # Perform element-wise addition with second array
        result_add = array1 + array2
        self.output.insert(tk.END, "Element-wise Addition (Array1 + Array2):\n")
        self.output.insert(tk.END, f"{result_add}\n\n")

        # Reshape the first array to 25x1
        reshaped_array = array1.reshape(25, 1)
        self.output.insert(tk.END, "Reshaped Array (25x1):\n")
        self.output.insert(tk.END, f"{reshaped_array}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ArrayApp(root)
    root.mainloop()