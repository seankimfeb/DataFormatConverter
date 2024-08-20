import tkinter as tk
from tkinter import filedialog
import os

def open_file(label, formattext, convertbutton):
    filetypes = [
        ('CSV files', '*.csv'),
        ('JSON files', '*.json'),
        ('Excel files', '*.xlsx'),
        ('XML files', '*.xml'),
        ('All files', '*.*'),
    ]
    format_mapping = {
        'csv': 'csv',
        'json': 'json',
        'xlsx': 'xlsx',
        'xml': 'xml'
    }
    
    filepath = filedialog.askopenfile(filetypes=filetypes)
    if filepath:
        label.config(text=filepath.name)
        _, file_extension = os.path.splitext(filepath.name)
        file_extension = file_extension.lower().strip('.')
        
        if file_extension in format_mapping:
            convertbutton.config(state=tk.NORMAL)
            file_format = "Selected Format: " + file_extension
            formattext.config(fg="black", bg="lightgreen")
        else:
            convertbutton.config(state=tk.DISABLED)
            file_format = "Selected Format: " + file_extension + " (Unsupported format)"
            formattext.config(fg="white", bg="red")
        
        formattext.config(text=file_format)
