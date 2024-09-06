import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pandas as pd

# Step 1: Clean the CSV data
def clean_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for i, line in enumerate(lines):
            if i == len(lines) - 1:  # Last line
                cleaned_line = line.rstrip(',\n')  # Remove comma and '\n' only in the last line
            else:
                if line.endswith(',\n'):
                    cleaned_line = line.rstrip(',\n') + '\n'
                else:
                    cleaned_line = line
            file.write(cleaned_line)

# Function to select the noise file
def select_noise_file():
    global noise_file_path
    noise_file_path = filedialog.askopenfilename(title="Select the noise file", filetypes=[("CSV files", "*.csv")])
    noise_label.config(text="Noise File: " + noise_file_path)

# Function to select the event file
def select_event_file():
    global event_file_path
    event_file_path = filedialog.askopenfilename(title="Select the check file", filetypes=[("CSV files", "*.csv")])
    event_label.config(text="Check File: " + event_file_path)

# Function to check and clean data
def check_files():
    try:
        clean_csv(noise_file_path)
        clean_csv(event_file_path)

        # Read the files
        noise_data = pd.read_csv(noise_file_path, dtype=str)
        event_data = pd.read_csv(event_file_path, dtype=str)

        # Compare and remove noise from event data
        columns_to_compare = ['ID', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8']
        noise_tuples = set(noise_data[columns_to_compare].apply(tuple, axis=1))
        event_tuples = event_data[columns_to_compare].apply(tuple, axis=1)

        # Find the clean rows
        cleaned_indexes = event_data[~event_tuples.isin(noise_tuples)].index

        # Display results in the interface
        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Initial number of rows in event data: {event_data.shape[0]}\n")
        result_text.insert(tk.END, f"Number of rows after removing noise: {len(cleaned_indexes)}\n")
        result_text.insert(tk.END, "Cleaned event data (rows without noise):\n")
        result_text.insert(tk.END, event_data.loc[cleaned_indexes].to_string(index=False))
        result_text.config(state='disabled')

        # Save the cleaned data
        global cleaned_event_data
        cleaned_event_data = event_data.loc[cleaned_indexes]

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to export the cleaned data to CSV
def export_csv():
    if 'cleaned_event_data' in globals():
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if save_path:
            cleaned_event_data.to_csv(save_path, index=False)
            messagebox.showinfo("Success", "File exported successfully!")
    else:
        messagebox.showwarning("Warning", "No cleaned data to export!")

# Function to reset the program state
def reset():
    result_text.config(state='normal')
    result_text.delete(1.0, tk.END)
    result_text.config(state='disabled')
    noise_label.config(text="Noise File: Not selected")
    event_label.config(text="Check File: Not selected")
    global noise_file_path, event_file_path
    noise_file_path, event_file_path = None, None

# Function to create rounded buttons
def create_rounded_button(text, command, row, column, color="#1E90FF"):
    button = tk.Button(root, text=text, command=command, bg=color, fg="white", font=("Helvetica", 10, "bold"), 
                       relief="flat", bd=0, padx=20, pady=5)
    button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
    button.config(highlightbackground=color)
    return button

# Main program settings
root = tk.Tk()
root.title("bolop CANBus")
root.geometry("800x600")
root.config(bg="#2C3E50")

# Responsive layout settings
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(4, weight=1)

# Program title
title_label = tk.Label(root, text="bolop CANBus", font=("Helvetica", 18, "bold"), fg="white", bg="#2C3E50")
title_label.grid(row=0, column=0, columnspan=3, pady=20, sticky="nsew")

# Section for selecting the noise file
create_rounded_button("Select the noise file", select_noise_file, 1, 0, color="#3498DB")
noise_label = tk.Label(root, text="Noise File: Not selected", font=("Helvetica", 10), fg="white", bg="#2C3E50")
noise_label.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="w")

# Section for selecting the event file
create_rounded_button("Select the check file", select_event_file, 2, 0, color="#3498DB")
event_label = tk.Label(root, text="Check File: Not selected", font=("Helvetica", 10), fg="white", bg="#2C3E50")
event_label.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="w")

# Main buttons
create_rounded_button("Let's check", check_files, 3, 0, color="#27AE60")
create_rounded_button("Export CSV", export_csv, 3, 1, color="#27AE60")
create_rounded_button("Reset", reset, 3, 2, color="#E74C3C")

# Terminal-style result display
result_text = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD, state='disabled', bg="black", fg="green", insertbackground="green", font=("Courier", 10, "bold"))
result_text.grid(row=4, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

# Run the program
root.mainloop()
