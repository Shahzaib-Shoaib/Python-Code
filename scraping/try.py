import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import os


def scrap(url):
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

    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, features="html.parser")

    # Extracting main product information
    product_data_divs = soup.find('div', class_='right-panel')
    product_name = product_data_divs.find(
        'h1', class_='pdp-title').get_text(strip=True)
    print(product_name)
    product_vendor = product_data_divs.find(
        'a', class_='rd-primary-link').get_text(strip=True)
    try:
        product_color = product_data_divs.find(
            'p', class_='size-color-info').get_text()
        match = color_pattern.search(product_color)
        color = match.group(1) if match else None
    except AttributeError:
        color = None

    # Extracting product description
    product_info_divs = soup.find('div', id='product-overview-container')

    product_description = product_info_divs.find(
        'div', class_='product-overview-data')

    # Extracting product metafields
    product_metafields = product_info_divs.find(
        'div', class_='rug-features-item')
    features_divs = product_metafields.find_all('div', class_='rug-features')

    features_dict = {}
    for feature in features_divs:
        key = feature.find(
            'div', class_='rug-features-left').get_text(strip=True)
        value = feature.find(
            'div', class_='rug-features-right').get_text(strip=True)
        transformed_metafield_key = key + " " + f"(product.metafields.custom.{
            key.replace(' ', '_').lower()})"

        features_dict[transformed_metafield_key] = value

    # Extracting product images
    product_image_div = soup.find('div', class_='MagicSlideshow')
    magic_zoom_links = product_image_div.find_all('a', class_='MagicZoom')
    image_urls = [link['href'] for link in magic_zoom_links]

    # Extracting variant information
    product_variant_divs = soup.find_all('div', class_='p-tile product_tile')
    count = 0

    for product_variant_div in product_variant_divs:
        if count < len(image_urls):
            url = image_urls[count]
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
                sale_price = match.group(2)
                original_price = match.group(3)
            else:
                sale_price = original_price = None
        except AttributeError:
            sale_price = original_price = None

        if len(image_urls) == 1:
            variant_image = image_urls[0]
        else:
            variant_image = image_urls[1]

        product_info = {
            'Title': product_name,
            'Body (HTML)': product_description,
            'Vendor': product_vendor,
            'Option1 Name': 'Color',
            'Option1 Value': color,
            'Option2 Name': "Size",
            'Option2 Value': size,
            'Variant Compare At Price': sale_price,
            'Variant Price': original_price,
            'Image Src': url,
            'Variant Image': variant_image,
            'Variant Inventory Qty': 1,
        }
        product_info.update(features_dict)

        # Converting the product info dictionary to a DataFrame
        new_df = pd.DataFrame([product_info])

        # Append the new data to the existing DataFrame
        existing_df = pd.concat([existing_df, new_df], ignore_index=True)

        if count != len(image_urls):
            url = image_urls[count]

            product_info = {
                'Title': product_name,
                'Body (HTML)': None,
                'Vendor': None,
                'Option1 Name': None,
                'Option1 Value': None,
                'Option2 Name': None,
                'Option2 Value': None,
                'Variant Compare At Price': None,
                'Variant Price': None,
                'Image Src': url,
                'Variant Image': None,
                'Variant Inventory Qty': None,
            }
            count += 1
        # Converting the product info dictionary to a DataFrame
        new_df = pd.DataFrame([product_info])

        # Append the new data to the existing DataFrame
        existing_df = pd.concat([existing_df, new_df], ignore_index=True)
    # Save the updated DataFrame back to the CSV file
    existing_df.to_csv(csv_file, index=False)

    print(existing_df)
    print("CSV file added successfully")


main_url = 'https://www.rugs-direct.com/Details/CalvinKleinHome-Volcanic-VLC01/147663'
response = requests.get(main_url)
html_content = response.text
soup = BeautifulSoup(html_content, features="html.parser")
product_data_divs = soup.find('div', class_='right-panel')


href_list = []

try:
    product_color_variants = product_data_divs.find_all(
        'a', {'data-slide-id': True})
    for a_tag in product_color_variants:
        href = a_tag.get('href')
        href_list.append("https://www.rugs-direct.com"+href)

except AttributeError:
    product_color_variants = None

if product_color_variants == []:
    scrap(main_url)
else:
    for i in range(len(href_list)):
        scrap(href_list[i])
