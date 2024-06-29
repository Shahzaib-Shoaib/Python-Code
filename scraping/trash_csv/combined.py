import pandas as pd
import os

file1 = 'C:\\Users\\shahz\\OneDrive\\Documents\\GitHub\\Python-Code\\scraping\\trash_csv\\colonial_mills_1.csv'
file2 = 'C:\\Users\\shahz\\OneDrive\\Documents\\GitHub\\Python-Code\\scraping\\trash_csv\\colonial_mills_2.csv'

# Check if files exist
if not os.path.isfile(file1):
    print(f"File not found: {file1}")
    exit(1)

if not os.path.isfile(file2):
    print(f"File not found: {file2}")
    exit(1)

# Load the CSV files into DataFrames
try:
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
except Exception as e:
    print(f"Error reading CSV files: {e}")
    exit(1)

# Concatenate the DataFrames
combined_df = pd.concat([df1, df2], ignore_index=True)
print(combined_df)

# Save the combined DataFrame to a new CSV file
output_file = 'combined.csv'
combined_df.to_csv(output_file, index=False)

print(f"Combined CSV saved as {output_file}")
