import tkinter as tk
from tkinter import filedialog
import os  # Import os for file extension extraction
def open_file(label,formattext,convertbutton):
    
    filetypes = [
        ('All files', '*.*'),
        ('CSV files', '*.csv'),
        ('JSON files', '*.json'),
        ('Excel files', '*.xlsx'),
        ('XML files','*.xml' )
    ]
    format_mapping = [
            '.csv',
            '.json',
            '.xlsx',
            '.xml'
    ]
    filepath = filedialog.askopenfile(filetypes=filetypes)
    if filepath:
        label.config(text=filepath.name)
        # Detect the file extension
        _, file_extension = os.path.splitext(filepath.name)
        file_format = "Selected Format: " +file_extension.lower().strip('.')        
        
        
    if file_extension in format_mapping:
            convertbutton.config(state=tk.NORMAL)  # Enable the button
            file_format = "Selected Format: " + file_extension
            formattext.config(fg="black", bg="lightgreen")
    else:
        convertbutton.config(state=tk.DISABLED)  # Disable the button
        file_format = "Selected Format: " + file_extension + " (Unsupported format)"
        formattext.config(fg="white", bg="red")

    # Update the format text
    formattext.config(text=file_format)