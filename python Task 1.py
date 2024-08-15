import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    
    # You can add validation and data handling here
    if name and email and age:
        messagebox.showinfo("Form Submitted", f"Name: {name}\nEmail: {email}\nAge: {age}")
    else:
        messagebox.showerror("Error", "All fields are required!")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place the name label and entry
name_label = tk.Label(root, text="Name")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the email label and entry
email_label = tk.Label(root, text="Email")
email_label.grid(row=1, column=0, padx=10, pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the age label and entry
age_label = tk.Label(root, text="Age")
age_label.grid(row=2, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
