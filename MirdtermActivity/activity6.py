# Ryan Francis Camcaho Romano
# Bachelor of Science in Computer Science - Third Year - Block B
# Programming Language 101 - Tu.Th 08:30 AM-10:00 AM ABa 101
# Instructor: Mr. Ian Godwin Agapito
# Activity 6 - Midterm Activity
# (Challenge): Create a function that takes two NumPy arrays and performs matrix multiplication, handling exceptions for mismatched dimensions.

# Matrix Multiplication Application
# Performs matrix multiplication between two NumPy arrays using a GUI interface
# Handles exceptions for mismatched dimensions

import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class MatrixMultiplicationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Multiplication")

        # Window setup
        window_width = 800
        window_height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Header
        tk.Label(root, text="Welcome!", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(root, text="Enter two matrices and perform matrix multiplication", 
                font=("Arial", 10)).pack()

        # Input frames
        input_frame = ttk.Frame(root)
        input_frame.pack(pady=10, fill=tk.X, padx=20)

        # Matrix A input
        matrix_a_frame = ttk.LabelFrame(input_frame, text="Matrix A")
        matrix_a_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
        
        tk.Label(matrix_a_frame, text="Enter values (space-separated rows, new line for each row):", 
                font=("Arial", 10)).pack(pady=5)
        
        self.matrix_a_input = scrolledtext.ScrolledText(matrix_a_frame, width=30, height=5, wrap=tk.WORD)
        self.matrix_a_input.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
        self.matrix_a_input.insert(tk.END, "1 2 3\n4 5 6")

        # Matrix B input
        matrix_b_frame = ttk.LabelFrame(input_frame, text="Matrix B")
        matrix_b_frame.pack(side=tk.RIGHT, padx=10, fill=tk.BOTH, expand=True)
        
        tk.Label(matrix_b_frame, text="Enter values (space-separated rows, new line for each row):", 
                font=("Arial", 10)).pack(pady=5)
        
        self.matrix_b_input = scrolledtext.ScrolledText(matrix_b_frame, width=30, height=5, wrap=tk.WORD)
        self.matrix_b_input.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
        self.matrix_b_input.insert(tk.END, "7 8\n9 10\n11 12")

        # Button styling
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 12), padding=10, background="#4CAF50", foreground="black")
        style.map("Custom.TButton", background=[("active", "#45a049")])

        # Buttons
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Multiply Matrices", style="Custom.TButton", 
                  command=self.perform_multiplication, width=25).pack(pady=5)
        
        ttk.Button(button_frame, text="Clear All", style="Custom.TButton", 
                  command=self.clear_all, width=25).pack(pady=5)

        # Output area
        tk.Label(root, text="Results:", font=("Arial", 12, "bold")).pack(pady=5)
        self.output = scrolledtext.ScrolledText(root, width=70, height=10, wrap=tk.WORD, font=("Arial", 12))
        self.output.pack(pady=10, fill=tk.BOTH, expand=True, padx=20)

        # Footer
        footer_frame = ttk.Frame(root)
        footer_frame.pack(side=tk.BOTTOM, pady=10, fill=tk.X)
        tk.Label(footer_frame, text="PL 101 - Midterm Activity 6", 
                font=("Arial", 10, "italic")).pack()

    def clear_output(self):
        self.output.delete(1.0, tk.END)
    
    def clear_all(self):
        self.matrix_a_input.delete(1.0, tk.END)
        self.matrix_b_input.delete(1.0, tk.END)
        self.clear_output()

    def parse_matrix(self, text_input):
        """Parse matrix from text input"""
        try:
            # Split by lines and then by spaces
            lines = text_input.strip().split('\n')
            matrix = []
            
            for line in lines:
                if line.strip():  # Skip empty lines
                    row = [float(x) for x in line.strip().split()]
                    matrix.append(row)
            
            # Check if all rows have the same number of elements
            if not all(len(row) == len(matrix[0]) for row in matrix):
                raise ValueError("All rows must have the same number of elements")
                
            return np.array(matrix)
        except ValueError as e:
            raise ValueError(f"Invalid matrix format: {str(e)}")
    
    def matrix_multiply(self, matrix_a, matrix_b):
        """
        Performs matrix multiplication between two NumPy arrays.
        Handles exceptions for mismatched dimensions.
        """
        try:
            # Check dimensions compatibility
            if matrix_a.shape[1] != matrix_b.shape[0]:
                raise ValueError(f"Matrix dimensions are incompatible for multiplication: "
                                f"{matrix_a.shape} and {matrix_b.shape}. "
                                f"The number of columns in Matrix A ({matrix_a.shape[1]}) must equal "
                                f"the number of rows in Matrix B ({matrix_b.shape[0]})")
            
            # Perform matrix multiplication
            result = np.matmul(matrix_a, matrix_b)
            return result
        
        except Exception as e:
            raise Exception(f"Multiplication error: {str(e)}")

    def perform_multiplication(self):
        """Read input matrices and perform multiplication"""
        self.clear_output()
        
        try:
            # Parse matrices from input
            matrix_a_text = self.matrix_a_input.get("1.0", tk.END)
            matrix_b_text = self.matrix_b_input.get("1.0", tk.END)
            
            matrix_a = self.parse_matrix(matrix_a_text)
            matrix_b = self.parse_matrix(matrix_b_text)
            
            # Display input matrices
            self.output.insert(tk.END, "Matrix A:\n")
            self.output.insert(tk.END, f"{matrix_a}\n\n")
            self.output.insert(tk.END, "Shape: " + str(matrix_a.shape) + "\n\n")
            
            self.output.insert(tk.END, "Matrix B:\n")
            self.output.insert(tk.END, f"{matrix_b}\n\n")
            self.output.insert(tk.END, "Shape: " + str(matrix_b.shape) + "\n\n")
            
            # Perform multiplication
            result = self.matrix_multiply(matrix_a, matrix_b)
            
            # Display result
            self.output.insert(tk.END, "Result (A × B):\n")
            self.output.insert(tk.END, f"{result}\n\n")
            self.output.insert(tk.END, "Shape: " + str(result.shape) + "\n\n")
            
            # Display properties
            self.output.insert(tk.END, "Properties:\n")
            self.output.insert(tk.END, f"Determinant (if square): {np.linalg.det(result) if result.shape[0] == result.shape[1] else 'N/A'}\n")
            self.output.insert(tk.END, f"Trace (if square): {np.trace(result) if result.shape[0] == result.shape[1] else 'N/A'}\n")
            self.output.insert(tk.END, f"Rank: {np.linalg.matrix_rank(result)}\n")
            
        except Exception as e:
            self.output.insert(tk.END, f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixMultiplicationApp(root)
    root.mainloop()