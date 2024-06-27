import pandas as pd

def delete_duplicate_rows_from_csv(csv_filename):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_filename)
    
    # Display initial DataFrame
    print("Initial DataFrame:")
    print(df)
    
    # Remove duplicate rows
    updated_df = df.drop_duplicates()
    
    # Display updated DataFrame
    print("Updated DataFrame:")
    print(updated_df)
    
    # Write the updated DataFrame back to the CSV file
    updated_df.to_csv(csv_filename, index=False)
    
    print("CSV file updated successfully")

# Example usage
delete_duplicate_rows_from_csv('product_details.csv')
