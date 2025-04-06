# Ryan Francis Camcaho Romano
# Bachelor of Science in Computer Science - Third Year - Block B
# Programming Language 101 - Tu.Th 08:30 AM-10:00 AM ABa 101
# Instructor: Mr. Ian Godwin Agapito
# Activity 4 - Midterm Activity
# (Pair Work): Compare different slicing and indexing techniques with a sample dataset.
# Ryan Francis Camcaho Romano & Marnie Delos Santos Indias



import numpy as np
import tkinter as tk
from tkinter import ttk, scrolledtext

import tkinter as tk
from tkinter import ttk, scrolledtext

class InputWindow:
    def __init__(self, parent, callback):
        self.window = tk.Toplevel(parent)
        self.window.title("Input Array")
        self.window.geometry("400x300")

        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        x = (screen_width // 2) - (400 // 2)
        y = (screen_height // 2) - (300 // 2)
        self.window.geometry(f"400x300+{x}+{y}")

        tk.Label(self.window, text="Enter array (space-separated rows, new line for each row):", 
                 font=("Arial", 10)).pack(pady=5)

        self.array_input = scrolledtext.ScrolledText(self.window, width=40, height=10, wrap=tk.WORD)
        self.array_input.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
        self.array_input.insert(tk.END, "120 150 180 200\n90 110 130 150\n200 220 240 260")

        ttk.Button(self.window, text="Submit", command=lambda: self.submit(callback)).pack(pady=10)
        ttk.Button(self.window, text="Clear All", command=self.clear_all).pack(pady=5)

    def submit(self, callback):
        array_text = self.array_input.get("1.0", tk.END)
        callback(array_text)
        self.window.destroy()

    def clear_all(self):
        self.array_input.delete("1.0", tk.END)

class ArraySlicingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compare Array Slicing and Indexing Techniques")

        window_width = 800
        window_height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Header
        tk.Label(root, text="Compare Array Slicing and Indexing Techniques", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(root, text="Explore different and compare NumPy array slicing and indexing techniques", 
                font=("Arial", 10)).pack()

        results_frame = ttk.Frame(root)
        results_frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)

        basic_frame = ttk.LabelFrame(results_frame, text="Basic Techniques")
        basic_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        self.basic_output = scrolledtext.ScrolledText(basic_frame, width=35, height=20, 
                                                    wrap=tk.WORD, font=("Arial", 10))
        self.basic_output.pack(pady=5, fill=tk.BOTH, expand=True)

        advanced_frame = ttk.LabelFrame(results_frame, text="Advanced Techniques")
        advanced_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        self.advanced_output = scrolledtext.ScrolledText(advanced_frame, width=35, height=20, 
                                                       wrap=tk.WORD, font=("Arial", 10))
        self.advanced_output.pack(pady=5, fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 12), padding=10, background="#4CAF50", foreground="black")
        style.map("Custom.TButton", background=[("active", "#45a049")])

        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Compare Random Array", style="Custom.TButton", 
                  command=self.compare_random, width=25).pack(pady=5)
        
        ttk.Button(button_frame, text="Input Array", style="Custom.TButton", 
                  command=self.open_input_window, width=25).pack(pady=5)
        
        ttk.Button(button_frame, text="Clear All", style="Custom.TButton", 
                  command=self.clear_all, width=25).pack(pady=5)

        footer_frame = ttk.Frame(root)
        footer_frame.pack(side=tk.BOTTOM, pady=6, fill=tk.X)
        ttk.Label(footer_frame, text="PL 101 - Midterm Activity 4(Pair work)", 
                 font=("Helvetica", 10, "italic")).pack()

    def clear_output(self):
        self.basic_output.delete(1.0, tk.END)
        self.advanced_output.delete(1.0, tk.END)

    def clear_all(self):
        self.clear_output()

    def parse_array(self, text_input):
        try:
            lines = text_input.strip().split('\n')
            array = []
            for line in lines:
                if line.strip():
                    row = [float(x) for x in line.strip().split()]
                    array.append(row)
            if not all(len(row) == len(array[0]) for row in array):
                raise ValueError("All rows must have the same number of elements")
            return np.array(array)
        except ValueError as e:
            raise ValueError(f"Invalid array format: {str(e)}")

    def display_slicing_results(self, arr):
        """Display various slicing and indexing techniques in two boxes"""
        self.clear_output()
        
        # Configure tags for bold text
        self.basic_output.tag_configure("bold", font=("Arial", 10, "bold"))
        self.advanced_output.tag_configure("bold", font=("Arial", 10, "bold"))
        
        # Basic Techniques
        self.basic_output.insert(tk.END, "Original Array:\n", "bold")
        self.basic_output.insert(tk.END, f"{arr}\n\n")
        
        self.basic_output.insert(tk.END, "Shape: ", "bold")
        self.basic_output.insert(tk.END, f"{arr.shape}\n\n")
        
        self.basic_output.insert(tk.END, "Basic Indexing:\n", "bold")
        self.basic_output.insert(tk.END, "First row: ", "bold")
        self.basic_output.insert(tk.END, f"{arr[0]}\n")
        self.basic_output.insert(tk.END, "First column: ", "bold")
        self.basic_output.insert(tk.END, f"{arr[:, 0]}\n\n")
        
        self.basic_output.insert(tk.END, "Slicing:\n", "bold")
        self.basic_output.insert(tk.END, "First 2 rows: \n", "bold")
        self.basic_output.insert(tk.END, f"{arr[:2]}\n")
        self.basic_output.insert(tk.END, "Last 2 columns: \n", "bold")
        self.basic_output.insert(tk.END, f"{arr[:, -2:]}\n")

        # Advanced Techniques
        self.advanced_output.insert(tk.END, "Advanced Indexing:\n", "bold")
        indices = [0, -1]
        self.advanced_output.insert(tk.END, "Selected rows (first and last): \n", "bold")
        self.advanced_output.insert(tk.END, f"{arr[indices]}\n\n")
        
        self.advanced_output.insert(tk.END, "Boolean Indexing:\n", "bold")
        mask = arr > np.mean(arr)
        self.advanced_output.insert(tk.END, "Values above mean: ", "bold")
        self.advanced_output.insert(tk.END, f"{arr[mask]}\n\n")
        
        self.advanced_output.insert(tk.END, "Combined Techniques:\n", "bold")
        increasing = np.all(np.diff(arr, axis=1) > 0, axis=1)
        self.advanced_output.insert(tk.END, "Rows with increasing values: \n", "bold")
        self.advanced_output.insert(tk.END, f"{arr[increasing]}\n")

    def compare_random(self):
        random_arr = np.random.randint(0, 100, size=(3, 4))
        self.display_slicing_results(random_arr)

    def open_input_window(self):
        InputWindow(self.root, self.process_input_array)

    def process_input_array(self, array_text):
        try:
            arr = self.parse_array(array_text)
            self.display_slicing_results(arr)
        except Exception as e:
            self.basic_output.insert(tk.END, f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ArraySlicingApp(root)
    root.mainloop()