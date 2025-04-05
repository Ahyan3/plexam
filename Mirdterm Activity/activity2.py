# Ryan Francis Camcaho Romano
# Bachelor of Science in Computer Science - Third Year - Block B
# Programming Language 101 - Tu.Th 08:30 AM-10:00 AM ABa 101
# Instructor: Mr. Ian Godwin Agapito
# Activity 2 - Midterm Activity
# (Individual): Create a NumPy array and print its properties (shape, data type, size).


import numpy as np  # NumPy for array operations
import tkinter as tk  # GUI creation
from tkinter import ttk, messagebox, scrolledtext  # Tkinter modules for styled widgets, message boxes, and scrollable text

class ArrayApp:
    def __init__(self, root):
        # Initialize the app with the main window (root)
        self.root = root
        self.root.title("Array Creator")  # Set the window title

        # Main window
        window_width = 600  
        window_height = 600 
        screen_width = root.winfo_screenwidth()  # Get screen width
        screen_height = root.winfo_screenheight()  # Get screen height
        x = (screen_width // 2) - (window_width // 2)  # Calculate x-coordinate for centering
        y = (screen_height // 2) - (window_height // 2)  # Calculate y-coordinate for centering
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Set window size and position

        tk.Label(root, text="Activity 2 -!", font=("Arial", 14, "bold")).pack(pady=10)  
        tk.Label(root, text="Create arrays and view their properties(shapes, data type, size).", font=("Arial", 10)).pack() 

        # Frame for option buttons
        self.option_frame = ttk.Frame(root)  # Frame to hold buttons
        self.option_frame.pack(pady=10)  # Place frame with padding

        # Custom button style
        style = ttk.Style()  # Create a style object
        style.configure("Custom.TButton", font=("Arial", 12), padding=10, background="#4CAF50", foreground="black")  # Set button properties (green background)
        style.map("Custom.TButton", background=[("active", "#45a049")])  # Change background on hover

        # Buttons, one per row, for different array creation options
        ttk.Button(self.option_frame, text="Manual Input (1D)", style="Custom.TButton", 
                  command=self.manual_input, width=25).pack(pady=5)  # Button for manual 1D array input
        ttk.Button(self.option_frame, text="Random Array (1D)", style="Custom.TButton", 
                  command=self.random_array, width=25).pack(pady=5)  # Button for random 1D array
        ttk.Button(self.option_frame, text="Range Array (1D)", style="Custom.TButton", 
                  command=self.range_array, width=25).pack(pady=5)  # Button for range-based 1D array
        ttk.Button(self.option_frame, text="Multi-Dimensional", style="Custom.TButton", 
                  command=self.multi_dimensional, width=25).pack(pady=5)  # Button for multi-dimensional array

        # Output area to display arrays and properties
        self.output = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD, font=("Arial", 12)) 
        self.output.pack(pady=10)  

        # Footer
        footer_frame = ttk.Frame(root)
        footer_frame.pack(side=tk.BOTTOM, pady=10, fill=tk.X)
        tk.Label(footer_frame, text="PL 101 - Midterm Activity 2", font=("Arial", 10, "italic")).pack() 

    def clear_output(self):
        # Clear the output text area
        self.output.delete(1.0, tk.END) 

    def display_array(self, array):
        # Display the created array and its properties in the output area
        self.clear_output()  # Clear previous output
        self.output.insert(tk.END, "Array created:\n")
        self.output.insert(tk.END, f"{array}\n\n") 
        self.output.insert(tk.END, "Array Properties:\n") 
        self.output.insert(tk.END, f"Shape: {array.shape}\n") 
        self.output.insert(tk.END, f"Data Type: {array.dtype}\n") 
        self.output.insert(tk.END, f"Size: {array.size}\n")

    def center_window(self, win, width, height):
        # Center a popup window on the screen
        screen_width = self.root.winfo_screenwidth()  
        screen_height = self.root.winfo_screenheight()  
        x = (screen_width // 2) - (width // 2)  # Calculate x-coordinate
        y = (screen_height // 2) - (height // 2)  # Calculate y-coordinate
        win.geometry(f"{width}x{height}+{x}+{y}")  # Set window size and position

    def manual_input(self):
        # Create a popup for manual 1D array input
        win = tk.Toplevel(self.root) 
        win.title("Manual Input (1D)") 
        self.center_window(win, 300, 200) 
        win.transient(self.root)  
        win.grab_set()  

        tk.Label(win, text="Enter values separated by spaces:", font=("Arial", 10)).pack(pady=5) 
        entry = ttk.Entry(win, width=30)
        entry.pack(pady=5)  

        def process():
            # Process the manual input and create array
            try:
                values = [float(x) for x in entry.get().split()]  # Convert input to list of floats
                array = np.array(values) 
                self.display_array(array)  
                win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter numeric values only.")

        ttk.Button(win, text="Create", command=process).pack(pady=10) 
        ttk.Button(win, text="Cancel", command=win.destroy).pack(pady=5) 

    def random_array(self):
        # Create a popup for random 1D array input
        win = tk.Toplevel(self.root) 
        win.title("Random Array (1D)")
        self.center_window(win, 300, 250)  
        win.transient(self.root)
        win.grab_set()

        tk.Label(win, text="Size:", font=("Arial", 10)).pack(pady=5)  
        size_entry = ttk.Entry(win, width=10)  
        size_entry.pack()  

        tk.Label(win, text="Minimum value:", font=("Arial", 10)).pack(pady=5) 
        min_entry = ttk.Entry(win, width=10) 
        min_entry.pack() 

        tk.Label(win, text="Maximum value:", font=("Arial", 10)).pack(pady=5) 
        max_entry = ttk.Entry(win, width=10) 
        max_entry.pack() 

        def process():
            # Process the random array input and create array
            try:
                size = int(size_entry.get())
                min_val = float(min_entry.get())
                max_val = float(max_entry.get())
                array = np.random.uniform(min_val, max_val, size) 
                self.display_array(array)
                win.destroy()  
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric values.") 

        ttk.Button(win, text="Create", command=process).pack(pady=10)  
        ttk.Button(win, text="Cancel", command=win.destroy).pack(pady=5) 

    def range_array(self):
        # Create a popup for range-based 1D array input
        win = tk.Toplevel(self.root) 
        win.title("Range Array (1D)")
        self.center_window(win, 300, 250) 
        win.transient(self.root) 
        win.grab_set()  

        tk.Label(win, text="Start value:", font=("Arial", 10)).pack(pady=5)  
        start_entry = ttk.Entry(win, width=10)  
        start_entry.pack()  

        tk.Label(win, text="End value:", font=("Arial", 10)).pack(pady=5)  
        end_entry = ttk.Entry(win, width=10) 
        end_entry.pack() 

        tk.Label(win, text="Step size:", font=("Arial", 10)).pack(pady=5) 
        step_entry = ttk.Entry(win, width=10) 
        step_entry.pack()

        def process():
            # Process the range input and create array
            try:
                start = int(start_entry.get()) 
                end = int(end_entry.get())  
                step = int(step_entry.get())
                array = np.arange(start, end, step)  
                self.display_array(array)  
                win.destroy() 
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric values.")  

        ttk.Button(win, text="Create", command=process).pack(pady=10) 
        ttk.Button(win, text="Cancel", command=win.destroy).pack(pady=5) 

    def multi_dimensional(self):
        # Create a popup for multi-dimensional array input
        win = tk.Toplevel(self.root)
        win.title("Multi-Dimensional Array")  
        self.center_window(win, 500, 400)  
        win.transient(self.root) 
        win.grab_set()  

        tk.Label(win, text="Enter dimensions (e.g., '2 3 4'):", font=("Arial", 10)).pack(pady=10)  # Label for dimensions
        dims_entry = ttk.Entry(win, width=40)  # Dimensions input field
        dims_entry.pack(pady=5)  # Place dimensions field

        tk.Label(win, text="Choose input method:", font=("Arial", 10)).pack(pady=10)  # Label for input method
        method = tk.StringVar(value="manual")  # Variable to track input method, default to manual
        ttk.Radiobutton(win, text="Manual Input", variable=method, value="manual").pack(pady=5)  # Manual input option
        ttk.Radiobutton(win, text="Random Values", variable=method, value="random").pack(pady=5)  # Random values option

        tk.Label(win, text="Values (for manual) or Min (for random):", font=("Arial", 10)).pack(pady=10)  # Label for values/min
        val1_entry = ttk.Entry(win, width=40)  # Values or min input field
        val1_entry.pack(pady=5)  # Place values/min field

        tk.Label(win, text="Max (for random only):", font=("Arial", 10)).pack(pady=10)  # Label for max (random only)
        val2_entry = ttk.Entry(win, width=10)  # Max value input field
        val2_entry.pack(pady=5)  # Place max field

        def process():
            # Process the multi-dimensional input and create array
            try:
                dim_list = [int(x) for x in dims_entry.get().split()]  # Convert dimensions to list of integers
                total_size = np.prod(dim_list)  # Calculate total number of elements

                if method.get() == "manual":
                    # Manual input: create array from user-provided values
                    values = [float(x) for x in val1_entry.get().split()]  # Convert input to list of floats
                    if len(values) != total_size:
                        messagebox.showerror("Error", f"Number of values ({len(values)}) must match size ({total_size})")  # Check size match
                        return
                    array = np.array(values).reshape(dim_list) 
                else:
                    # Random values: create array with random numbers
                    min_val = float(val1_entry.get())  
                    max_val = float(val2_entry.get()) 
                    array = np.random.uniform(min_val, max_val, dim_list)  

                self.display_array(array) 
                win.destroy()  
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric values.") 

        ttk.Button(win, text="Create", command=process).pack(pady=10)  
        ttk.Button(win, text="Cancel", command=win.destroy).pack(pady=5) 

if __name__ == "__main__":
    # Main execution block: start the app
    root = tk.Tk()  # Create the main Tkinter window
    app = ArrayApp(root)  # Instantiate the app
    root.mainloop()  # Run the Tkinter event loop