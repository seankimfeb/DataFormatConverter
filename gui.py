import tkinter as tk
from tkinter import ttk
from file_selector import open_file
from converter import testingconvert

def create_main_window():
    window = tk.Tk()
    window.title("Data Format Converter")
    window.geometry("400x300")
    

    # Create a label to show the selected file path
    selected_file_label = tk.Label(window, text="No file selected")
    selected_file_label.pack(pady=10)
    
    formatconfirm = tk.Label(window, text="")
    formatconfirm.pack(pady=10)

    # Create a button to open the file dialog
    open_button = tk.Button(window, text="Open File",command=lambda: open_file(selected_file_label,formatconfirm,convert_button))
    open_button.pack(pady=10)
    combo = ttk.Combobox(window, values=["CSV", "JSON", "XML", "XLSX"])
    combo.pack(pady=20)
    convert_button = tk.Button(window,text="Convert!",command=lambda: testingconvert(selected_file_label.cget("text")))
    convert_button.pack(pady=20)
    

    

    return window