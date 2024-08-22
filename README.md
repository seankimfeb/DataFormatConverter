
# Data Format Converter

A simple Python application that converts data between CSV, JSON, XML, and XLSX formats using `pandas` and `tkinter`.

## Features

- Convert files between multiple formats.
- Simple and user-friendly GUI built with `tkinter`.
- Supports CSV, JSON, XML, and XLSX formats.

## Requirements

Before running the application, ensure you have the following Python packages installed:

```bash
pip install pandas openpyxl lxml

git clone https://github.com/yourusername/DataFormatConverter.git
cd DataFormatConverter

Install Dependencies:
Ensure you have Python installed. Then, install the required Python libraries:

pip install pandas openpyxl
Optional - For XML Conversion:
If you plan to convert files to XML, install the lxml library:

pip install lxml

## Usage
Run the Application:

python main.py
Use the Interface:

Open File: Click the "Open File" button to select your input file.
Select Output Format: Choose the desired output format from the dropdown menu.
Convert: Click the "Convert!" button to start the conversion. A success message will appear if the conversion is successful.
Locate Converted File:
The converted file will be saved in the same directory as the original input file.

Example Files
CSV:

Username; Identifier; First name; Last name
booker12; 9012; Rachel; Booker
grey07; 2070; Laura; Grey
johnson81; 4081; Craig; Johnson
jenkins46; 9346; Mary; Jenkins
smith79; 5079; Jamie; Smith
JSON:

[
  {"Username": "booker12", "Identifier": 9012, "First name": "Rachel", "Last name": "Booker"},
  {"Username": "grey07", "Identifier": 2070, "First name": "Laura", "Last name": "Grey"},
  {"Username": "johnson81", "Identifier": 4081, "First name": "Craig", "Last name": "Johnson"},
  {"Username": "jenkins46", "Identifier": 9346, "First name": "Mary", "Last name": "Jenkins"},
  {"Username": "smith79", "Identifier": 5079, "First name": "Jamie", "Last name": "Smith"}
]
