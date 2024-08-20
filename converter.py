import tkinter as tk
import pandas as pd
import json, os, csv

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
        
        if outputformat == "xml":
            outputname = filename + ".xml"
            df.to_xml(outputname, root_name='root', row_name='row', index=False)
        
        elif outputformat == "json":
            outputname = filename + ".json"
            df.to_json(outputname, orient='records')
        
        elif outputformat == "xlsx":
            outputname = filename + ".xlsx"
            df.to_excel(outputname, index=False)
            
        print("Conversion successful")
    except ValueError as e:
        print(f"Conversion failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

        


def convert_json(filepath, outputformat, filename):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)  # Load JSON data
        
        # If data is a dictionary (single record), wrap it in a list
        if isinstance(data, dict):
            data = [data]
        
        # Convert the data to a DataFrame
        df = pd.DataFrame(data)
        
        if outputformat == "xml":
            outputname = filename + ".xml"
            df.to_xml(outputname, orient='records', index=False)
            print("Conversion successful")
        
        elif outputformat == "csv":
            outputname = filename + ".csv"
            df.to_csv(outputname, index=False)
            print("Conversion successful")
        
        elif outputformat == "xlsx":
            outputname = filename + ".xlsx"
            df.to_excel(outputname, index=False)
            print("Conversion successful")
        
        
    
    except ValueError as e:
        print(f"Conversion failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
##for testing, add parameters later
#def convert_json(filepath):
#    df = pd.read_json(filepath)
def testingconvert(filepath):
    try:
        # Load the JSON file
        with open(filepath, 'r') as file:
            data = json.load(file)

        # If data is a dictionary (single record), wrap it in a list
        if isinstance(data, dict):
            data = [data]

        # Now convert the data to a DataFrame
        df = pd.DataFrame(data)

        # Convert the DataFrame to CSV
        outputname = "output.csv"
        df.to_csv(outputname, index=False)
        print("Conversion successful")

    except ValueError as e:
        print(f"Conversion failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")