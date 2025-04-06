# Ryan Francis Camcaho Romano
# Bachelor of Science in Computer Science - Third Year - Block B
# Programming Language 101 - Tu.Th 08:30 AM-10:00 AM ABa 101
# Instructor: Mr. Ian Godwin Agapito
# Activity 1 - Midterm Activity
# Install NumPy and verify the installation.


#Open Terminal and run the following command to install numpy
#pip install numpy 
#python
#python --version





import tkinter as tk
import numpy as np
from tkinter import ttk

def show_version():
    version_label.config(text=f"NumPy Version: {np.__version__}")
    version_label.pack()  
    app.after(10000, lambda: version_label.pack_forget())

def center_window(window, width=300, height=180):  
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

app = tk.Tk()
app.title("NumPy Version Checker")
app.resizable(False, False)

center_window(app, 300, 180)

welcome_label = tk.Label(app, text="Check Your NumPy Version", font=("Arial", 12))
welcome_label.pack(pady=10)

check_button = tk.Button(app, text="Show NumPy Version", command=show_version)
check_button.pack(pady=5)

version_label = tk.Label(app, text="", font=("Arial", 10))

footer_frame = ttk.Frame(app)
footer_frame.pack(side=tk.BOTTOM, pady=10)
tk.Label(footer_frame, text="PL 101 - Midterm Activity 1", font=("Arial", 10, "italic")).pack()

app.mainloop()





#import numpy
#print(numpy.__version__)
#print("This is the NumPy version installed on your system.")

# or 

#import numpy as np
#array = np.array([1, 2, 3, 4])
#print("NumPy is working! Here's an array:", array)