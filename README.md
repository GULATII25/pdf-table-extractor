# PDF Table Extractor

## About This Project
A simple command-line script, built in Python, that extracts tables from PDF documents. Using the powerful `camelot-py` library, this tool parses a PDF file and saves each table it finds as a separate, clean CSV file.

## How to Use
1.  Download the project files.
2.  Make sure you have the necessary libraries installed by running `pip install "camelot-py[cv]"`.
3.  Place the PDF you want to analyze in the folder and rename it to `sample.pdf`.
4.  Run the script from your terminal with the command: `python3 extractor.py`
5.  The script will create a new folder named `extracted_tables` containing the results as CSV files.
