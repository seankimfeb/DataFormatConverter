import tkinter as tk
import pandas as pd
import json, os, csv
def show_success_message(i):
    # Create a new window for the success message
    success_window = tk.Toplevel()
    if(i==1):
        success_window.title("Success")
    else:
        success_window.title("Failure")
    
    # Set the size of the window
    success_window.geometry("200x100")
    
    # Create a label with the success message
    if(i==1):
        message_label = tk.Label(success_window, text="Conversion Successful!", font=("Arial", 12))
    else:
        message_label = tk.Label(success_window, text="Conversion Failed!", font=("Arial", 12))
    message_label.pack(pady=10)
    
    # Create a close button
    close_button = tk.Button(success_window, text="Close", command=success_window.destroy)
    close_button.pack(pady=10)
    
    # Run the window's main loop
    success_window.mainloop()

def convert_format(inputformat, filepath, outputformat, filename):
    try:
        # Handle different input formats
        if inputformat.lower() == "json":
            convert_json(filepath, outputformat, filename)
        elif inputformat.lower() == "csv":
            convert_csv(filepath, outputformat, filename)    
        # Add other formats if needed
        else:
            print(f"Input format '{inputformat}' is not supported.")
    except Exception as e:
        print(f"An error occurred: {e}")
##helper functions
def convert_csv(filepath, outputformat, filename):
    try:
        # Read CSV file
        df = pd.read_csv(filepath)
        
        # Extract the directory from the input file path
        directory = os.path.dirname(filepath)
        
        # Construct the output file path
        outputname = os.path.join(directory, filename)
        
        if outputformat == "xml":
            outputfile = outputname + ".xml"
            df.to_xml(outputfile, root_name='root', row_name='row', index=False)
        
        elif outputformat == "json":
            outputfile = outputname + ".json"
            df.to_json(outputfile, orient='records')
        
        elif outputformat == "xlsx":
            outputfile = outputname + ".xlsx"
            df.to_excel(outputfile, index=False)
            
        print("Conversion successful")
        show_success_message(1)
    except ValueError as e:
        print(f"Conversion failed: {e}")
        show_success_message(2)
    except Exception as e:
        print(f"An error occurred: {e}")
        show_success_message(2)

        


def convert_json(filepath, outputformat, filename):
    try:
        # Load JSON data
        with open(filepath, 'r') as file:
            data = json.load(file)
        
        # If data is a dictionary (single record), wrap it in a list
        if isinstance(data, dict):
            data = [data]
        
        # Convert the data to a DataFrame
        df = pd.DataFrame(data)
        
        # Extract the directory from the input file path
        directory = os.path.dirname(filepath)
        
        # Construct the output file path
        outputname = os.path.join(directory, filename)
        
        if outputformat == "xml":
            outputfile = outputname + ".xml"
            df.to_xml(outputfile, orient='records', index=False)
            print("Conversion successful")
        
        elif outputformat == "csv":
            outputfile = outputname + ".csv"
            df.to_csv(outputfile, index=False)
            print("Conversion successful")
        
        elif outputformat == "xlsx":
            outputfile = outputname + ".xlsx"
            df.to_excel(outputfile, index=False)
            print("Conversion successful")
        show_success_message(1)
    except ValueError as e:
        print(f"Conversion failed: {e}")
        show_success_message(2)
    except Exception as e:
        print(f"An error occurred: {e}")
        show_success_message(2)

