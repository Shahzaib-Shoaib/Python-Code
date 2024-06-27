import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.rugs-direct.com/Details/AmerRugs-Legacy-Barton/145273'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, features="html.parser")
pattern = re.compile(
    r'(\d+% Off)\$(\d{1,3}(?:,\d{3})*\.\d{2})\$(\d{1,3}(?:,\d{3})*\.\d{2})')
color_pattern = re.compile(r'Color:\s*(.*)')

product_data_divs = soup.find('div', class_='right-panel')

product_list = []

product_name = product_data_divs.find(
    'h1', class_='pdp-title').get_text(strip=True)
product_vendor = product_data_divs.find(
    'a', class_='rd-primary-link').get_text(strip=True)
product_color = product_data_divs.find(
    'p', class_='size-color-info mb-p5').get_text()
match = color_pattern.search(product_color)
if match:
    color = match.group(1)

product_info_divs = soup.find('div', id='product-overview-container')

product_description = product_info_divs.find(
    'div', class_='product-overview-data')
product_metafields = product_info_divs.find(
    'div', class_='rug-features-item')
features_divs = product_metafields.find_all('div', class_='rug-features')

features_dict = {}
for feature in features_divs:
    key = feature.find('div', class_='rug-features-left').get_text(strip=True)
    value = feature.find(
        'div', class_='rug-features-right').get_text(strip=True)
    transformed_metafield_key = key + " " + f"(product.metafields.custom.{
        key.replace(' ', '_').lower()})"
    print(transformed_metafield_key)

    features_dict[transformed_metafield_key] = value


product_variant_divs = soup.find_all('div', class_='p-tile product_tile')

product_image_div = soup.find('div', class_='MagicSlideshow')

magic_zoom_links = product_image_div.find_all('a', class_='MagicZoom')

image_urls = [link['href'] for link in magic_zoom_links]
count = 0

for product_variant_div in product_variant_divs:

    if count < len(image_urls):
        url = image_urls[count]
        count = count+1

    try:
        product_variant_size = product_variant_div.find(
            'div', class_='product_size')
        span_texts = [span.get_text(strip=True)
                      for span in product_variant_size.find('span')]
        for text in span_texts:
            size = text

    except AttributeError:
        product_variant_size = None

    try:
        product_variant_price = product_variant_div.find(
            'div', class_='product_sale').get_text(strip=True)
        match = pattern.match(product_variant_price)
        if match:
            discount_percent = match.group(1)
            sale_price = match.group(2)
            original_price = match.group(3)

    except AttributeError:
        product_variant_price = None

    product_variant_info = {
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
        'Variant Image': image_urls[1],
        'Variant Inventory Qty': 1,


    }
    product_variant_info.update(features_dict)
    product_list.append(product_variant_info)
    if count != len(image_urls):
        url = image_urls[count]

        product_variant_info = {
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
        count = count + 1
        product_list.append(product_variant_info)

    # product_image_info = {
    #     'Image Src': url,
    #     'Image Position': image_count
    # }
    # product_list.append(product_image_info)


df = pd.DataFrame(product_list)

df.to_csv('product_details.csv', index=False)

print(df)

# print("CSV file created successfully")
