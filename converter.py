import tkinter as tk
import pandas as pd
import json
#def convert_format(format,filepath,outputformat):
    #if(format == ".csv"):

##helper functions
def convert_csv(filepath,outputformat,filename):
    df = pd.read_csv(filepath)
    if(outputformat =="JSON"):
        outputname = filename + ".json"
        df.to_json(outputname,orient='records', lines=True)
    elif(outputformat == "XML"):
        outputname = filename + ".xml"
        df.to_xml(outputname,orient='records', lines=True)
    
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