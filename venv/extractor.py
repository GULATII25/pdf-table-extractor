import camelot
import pandas as pd
import os

def extract_tables_from_pdf(pdf_path, output_dir):
    """
    Extracts all tables from a given PDF file and saves them as CSV files.

    Args:
        pdf_path (str): The path to the input PDF file.
        output_dir (str): The directory where CSV files will be saved.
    """
    # Check if the PDF file exists
    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' was not found.")
        return

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Extracting tables from '{pdf_path}'...")
    
    # Read tables from the PDF
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='lattice')
    
    print(f"Found {tables.n} tables.")

    # Export each table to a CSV file
    for i, table in enumerate(tables):
        csv_filename = os.path.join(output_dir, f"table_{i+1}.csv")
        table.to_csv(csv_filename, index=False)
        print(f"Table {i+1} saved to '{csv_filename}'")

if __name__ == "__main__":
    pdf_file = "sample.pdf"
    output_folder = "extracted_tables"
    
    extract_tables_from_pdf(pdf_file, output_folder)import camelot
import pandas as pd
import os

def extract_tables_from_pdf(pdf_path, output_dir):
    """
    Extracts all tables from a given PDF file and saves them as CSV files.

    Args:
        pdf_path (str): The path to the input PDF file.
        output_dir (str): The directory where CSV files will be saved.
    """
    # Check if the PDF file exists
    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' was not found.")
        return

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Extracting tables from '{pdf_path}'...")
    
    # Read tables from the PDF
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='lattice')
    
    print(f"Found {tables.n} tables.")

    # Export each table to a CSV file
    for i, table in enumerate(tables):
        csv_filename = os.path.join(output_dir, f"table_{i+1}.csv")
        table.to_csv(csv_filename, index=False)
        print(f"Table {i+1} saved to '{csv_filename}'")

if __name__ == "__main__":
    pdf_file = "sample.pdf"
    output_folder = "extracted_tables"
    
    extract_tables_from_pdf(pdf_file, output_folder)