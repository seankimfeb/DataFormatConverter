import tkinter as tk
from tkinter import ttk
from file_selector import open_file
from converter import testingconvert

def create_main_window():
    window = tk.Tk()
    window.title("Data Format Converter")
    window.geometry("400x300")
    
    # Main Frame with background color
    main_frame = tk.Frame(window, padx=20, pady=20, bg='#f5f5f5')
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Add a title label at the top
    title_label = tk.Label(main_frame, text="Data Format Converter", font=("Arial", 16, 'bold'), bg='#f5f5f5', fg='#333333')
    title_label.pack(pady=(0, 20))

    # File Selection Section with border and background color
    file_frame = tk.Frame(main_frame, bg='#ffffff', padx=10, pady=10, borderwidth=2, relief='groove')
    file_frame.pack(pady=(0, 10))

    selected_file_label = tk.Label(file_frame, text="No file selected", font=("Arial", 12), bg='#ffffff')
    selected_file_label.pack(pady=(0, 5))

    formatconfirm = tk.Label(file_frame, text="", font=("Arial", 12), bg='#ffffff')
    formatconfirm.pack()

    open_button = tk.Button(file_frame, text="Open File", command=lambda: open_file(selected_file_label, formatconfirm, convert_button), bg='#4CAF50', fg='white', font=("Arial", 12, 'bold'))
    open_button.pack(pady=(10, 20))

    # Format and Convert Section with background color
    convert_frame = tk.Frame(main_frame, bg='#f5f5f5')
    convert_frame.pack()

    combo = ttk.Combobox(convert_frame, values=["CSV", "JSON", "XML", "XLSX"], state='readonly')
    combo.set("CSV")  # Set default value
    combo.pack(pady=(0, 10))

    convert_button = tk.Button(convert_frame, text="Convert!", command=lambda: testingconvert(selected_file_label.cget("text")), state=tk.DISABLED, bg='#2196F3', fg='white', font=("Arial", 12, 'bold'))
    convert_button.pack(pady=(10, 0))

    return window

if __name__ == "__main__":
    create_main_window().mainloop()
