# Ryan Francis Camcaho Romano
# Bachelor of Science in Computer Science - Third Year - Block B
# Programming Language 101 - Tu.Th 08:30 AM-10:00 AM ABa 101
# Instructor: Mr. Ian Godwin Agapito
# Activity 5 - Midterm Activity
# (Individual): Write a function that:
# Takes a NumPy array as input.
# Normalizes its values to a range between 0 and 1.
# Returns the modified array.



import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class ArrayNormalizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Array Normalization")

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
        tk.Label(root, text="Normalize array values to a range between 0 and 1", 
                font=("Arial", 10)).pack()

        # Option frame
        self.option_frame = ttk.Frame(root)
        self.option_frame.pack(pady=10)

        # Button styling
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 12), padding=10, background="#4CAF50", foreground="black")
        style.map("Custom.TButton", background=[("active", "#45a049")])

        # Buttons
        ttk.Button(self.option_frame, text="Random Array", style="Custom.TButton", 
                  command=self.generate_random_array, width=25).pack(pady=5)  
        ttk.Button(self.option_frame, text="Input Array", style="Custom.TButton", 
                  command=self.input_array, width=25).pack(pady=5)

        # Output area
        self.output = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD, font=("Arial", 12))
        self.output.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)

        # Footer
        footer_frame = ttk.Frame(root)
        footer_frame.pack(side=tk.BOTTOM, pady=10, fill=tk.X)
        tk.Label(footer_frame, text="PL 101 - Midterm Activity 5", 
                font=("Arial", 10, "italic")).pack()

    def clear_output(self):
        self.output.delete(1.0, tk.END)

    def normalize_array(self, array):
        """
        Normalizes array values to a range between 0 and 1.
        
        Parameters:
        array (numpy.ndarray): Input array
        
        Returns:
        numpy.ndarray: Normalized array
        """
        try:
            # Find min and max values
            min_val = np.min(array)
            max_val = np.max(array)
            
            # Check if array has a constant value (avoid division by zero)
            if min_val == max_val:
                # All values are the same, return an array of 0s or 1s
                if min_val == 0:
                    return np.zeros_like(array)
                else:
                    return np.ones_like(array)
            
            # Normalize to [0, 1]
            normalized = (array - min_val) / (max_val - min_val)
            
            return normalized
            
        except Exception as e:
            raise Exception(f"Normalization error: {str(e)}")

    def display_array(self, original_array, normalized_array):
        """Display original and normalized arrays"""
        self.clear_output()
        
        # Original array
        self.output.insert(tk.END, "Original Array:\n")
        self.output.insert(tk.END, f"{original_array}\n\n")
        self.output.insert(tk.END, f"Min value: {np.min(original_array)}\n")
        self.output.insert(tk.END, f"Max value: {np.max(original_array)}\n")
        self.output.insert(tk.END, f"Mean: {np.mean(original_array):.4f}\n\n")
        
        # Normalized array  
        self.output.insert(tk.END, "Normalized Array (0 to 1):\n")
        self.output.insert(tk.END, f"{normalized_array}\n\n")
        self.output.insert(tk.END, f"Min value: {np.min(normalized_array):.4f}\n")
        self.output.insert(tk.END, f"Max value: {np.max(normalized_array):.4f}\n")
        self.output.insert(tk.END, f"Mean: {np.mean(normalized_array):.4f}\n\n")
        
        # Array properties
        self.output.insert(tk.END, "Array Properties:\n")
        shape_str = f"(1, {original_array.shape[0]})" if len(original_array.shape) == 1 else str(original_array.shape)
        self.output.insert(tk.END, f"Shape: {shape_str}\n")
        self.output.insert(tk.END, f"Data Type: {original_array.dtype}\n")
        self.output.insert(tk.END, f"Size: {original_array.size}\n")

    def center_window(self, win, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        win.geometry(f"{width}x{height}+{x}+{y}")
    
    def generate_random_array(self):
        """Generate a random array and normalize it"""
        try:
            # Generate random array with values between -100 and 100
            array = np.random.uniform(-100, 100, 10)
            
            # Normalize array
            normalized = self.normalize_array(array)
            
            # Display results
            self.display_array(array, normalized)
            
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def input_array(self):
        """Create dialog for user input array"""
        win = tk.Toplevel(self.root)
        win.title("Input Array")
        self.center_window(win, 500, 200)
        win.transient(self.root)
        win.grab_set()

        tk.Label(win, text="Enter numeric values separated by spaces:", 
                font=("Arial", 10)).pack(pady=10)
        
        entry = ttk.Entry(win, width=50)
        entry.pack(pady=5)
        entry.focus_set()

        def process():
            input_str = entry.get().strip()
            if not input_str:
                messagebox.showerror("Error", "Please enter values")
                return
            
            try:
                # Parse input into array
                values = [float(x) for x in input_str.split()]
                array = np.array(values)
                
                # Normalize array
                normalized = self.normalize_array(array)
                
                win.destroy()  # Close the window first
                
                # Display results
                self.display_array(array, normalized)
                
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numeric values")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        ttk.Button(win, text="Process", command=process).pack(pady=5)
        ttk.Button(win, text="Cancel", command=win.destroy).pack(pady=5)
        
        # Handle Enter key
        win.bind('<Return>', lambda event: process())

if __name__ == "__main__":
    root = tk.Tk()
    app = ArrayNormalizationApp(root)
    root.mainloop()