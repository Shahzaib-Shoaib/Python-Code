import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import os

# List of URLs to process
urls = [
    "https://www.rugs-direct.com/Details/AmerRugs-Legacy-Barton/145273",
    "https://www.rugs-direct.com/Details/AmerRugs-Blend-Warwick/125203",
    "https://www.rugs-direct.com/Details/AmerRugs-Berlin-Drayton/145259",
    "https://www.rugs-direct.com/Details/AmerRugs-Vista-Duncan/145286/233435",
    "https://www.rugs-direct.com/Details/AmerRugs-Prairie-Camil/139180",
    "https://www.rugs-direct.com/Details/AmerRugs-Prairie-Shay/139181",
    "https://www.rugs-direct.com/Details/AmerRugs-Boscage-Ilford/142539/229438",
    "https://www.rugs-direct.com/Details/AmerRugs-Arizona-Cameron/113192/180841",
    "https://www.rugs-direct.com/Details/AmerRugs-Raffia-Rafaele/125300/201652",
    "https://www.rugs-direct.com/Details/AmerRugs-Abstract-Hammond/142573/229524",
    "https://www.rugs-direct.com/Details/AmerRugs-Blend-BLN15/125202",
    "https://www.rugs-direct.com/Details/AmerRugs-Hermitage-Alyanna/150077",
    "https://www.rugs-direct.com/Details/AmerRugs-Dune-Estra/150076",
    "https://www.rugs-direct.com/Details/AmerRugs-Dune-Cresa/150075",
    "https://www.rugs-direct.com/Details/AmerRugs-Berlin-Lanmore/145260",
    "https://www.rugs-direct.com/Details/AmerRugs-Alexandria-Aletha/133549/214463",
    "https://www.rugs-direct.com/Details/AmerRugs-Dune-Alliya/150074",
    "https://www.rugs-direct.com/Details/AmerRugs-Vista-Raton/145287/233438",
    "https://www.rugs-direct.com/Details/AmerRugs-Empress-Kingsley/130902",
    "https://www.rugs-direct.com/Details/AmerRugs-Eternal-ETE22/136135"
]

# Define the CSV file name
csv_file = 'product_details.csv'

# Check if the CSV file already exists
if os.path.isfile(csv_file):
    # If the file exists, read the existing data into a DataFrame
    existing_df = pd.read_csv(csv_file)
else:
    # If the file does not exist, create an empty DataFrame
    existing_df = pd.DataFrame()

# Patterns for extracting data
pattern = re.compile(
    r'(\d+% Off)\$(\d{1,3}(?:,\d{3})*\.\d{2})\$(\d{1,3}(?:,\d{3})*\.\d{2})')
color_pattern = re.compile(r'Color:\s*(.*)')

# Process each URL
for url in urls:
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, features="html.parser")

    # Extracting main product information
    product_data_divs = soup.find('div', class_='right-panel')
    product_name = product_data_divs.find(
        'h1', class_='pdp-title').get_text(strip=True)
    product_vendor = product_data_divs.find(
        'a', class_='rd-primary-link').get_text(strip=True)
    try:
        product_color = product_data_divs.find(
            'p', class_='size-color-info').get_text()
        match = color_pattern.search(product_color)
        color = match.group(1) if match else None
    except AttributeError:
        color = None

    # Initialize the product info dictionary

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

        product_info = {
            'Title': product_name,
            'Vendor': product_vendor,
            'Option1 Name': 'Color',
            'Option1 Value': color,
            'Option2 Name': "Size",
            'Option2 Value': size,
            'Variant Compare At Price': sale_price,
            'Variant Price': original_price,
            # 'Variant %d Discount Percent' % (count): discount_percent,

        }

        # Converting the product info dictionary to a DataFrame
        new_df = pd.DataFrame([product_info])

        # Append the new data to the existing DataFrame
        existing_df = pd.concat([existing_df, new_df], ignore_index=True)

# Save the updated DataFrame back to the CSV file
existing_df.to_csv(csv_file, index=False)

print(existing_df)
print("CSV file updated successfully")
