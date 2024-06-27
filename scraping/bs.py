import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import os

# URL of the product
url = 'https://www.rugs-direct.com/Details/AmerRugs-Legacy-Barton/145273'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, features="html.parser")

# Patterns for extracting data
pattern = re.compile(
    r'(\d+% Off)\$(\d{1,3}(?:,\d{3})*\.\d{2})\$(\d{1,3}(?:,\d{3})*\.\d{2})')
color_pattern = re.compile(r'Color:\s*(.*)')

# Extracting main product information
product_data_divs = soup.find('div', class_='right-panel')
product_name = product_data_divs.find(
    'h1', class_='pdp-title').get_text(strip=True)
product_vendor = product_data_divs.find(
    'a', class_='rd-primary-link').get_text(strip=True)
product_color = product_data_divs.find(
    'p', class_='size-color-info mb-p5').get_text()
match = color_pattern.search(product_color)
color = match.group(1) if match else None

# Initialize the product info dictionary
product_info = {
    'Product Name': product_name,
    'Vendor': product_vendor,
    'Color': color
}

# Extracting variant information
product_variant_divs = soup.find_all('div', class_='p-tile product_tile')
count = 0

for product_variant_div in product_variant_divs:
    count += 1
    try:
        product_variant_size = product_variant_div.find(
            'div', class_='product_size')
        size = product_variant_size.find('span').get_text(strip=True)
    except AttributeError:
        size = None

    try:
        product_variant_price = product_variant_div.find(
            'div', class_='product_sale').get_text(strip=True)
        match = pattern.match(product_variant_price)
        if match:
            discount_percent = match.group(1)
            sale_price = match.group(2)
            original_price = match.group(3)
        else:
            discount_percent = sale_price = original_price = None
    except AttributeError:
        discount_percent = sale_price = original_price = None

    # Adding variant information to the product info dictionary
    product_info[f'Variant {count} Size'] = size
    product_info[f'Variant {count} Discount Percent'] = discount_percent
    product_info[f'Variant {count} Sale Price'] = sale_price
    product_info[f'Variant {count} Original Price'] = original_price


# Converting the product info dictionary to a DataFrame
new_df = pd.DataFrame([product_info])

# Define the CSV file name
csv_file = 'product_details.csv'

# Check if the CSV file already exists
if os.path.isfile(csv_file):
    # If the file exists, read the existing data into a DataFrame
    existing_df = pd.read_csv(csv_file)
    # Append the new data to the existing DataFrame
    updated_df = pd.concat([existing_df, new_df], ignore_index=True)
else:
    # If the file does not exist, the updated DataFrame is just the new data
    updated_df = new_df

# Save the updated DataFrame back to the CSV file
updated_df.to_csv(csv_file, index=False)

print(updated_df)
