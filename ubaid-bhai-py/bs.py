import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.rugs-direct.com/Store/nav/Category-Area-Rugs-CustomSizes-Yes'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, features="html.parser")

product_data_divs = soup.find_all('div', class_='rd-card-body rd-product-data')
product_list = []

# Step 3: Iterate through all found divs and extract the relevant information
for product_data_div in product_data_divs:
    product_name = product_data_div.find(
        'a', class_='style').get_text(strip=True)
    brand = product_data_div.find('p', class_='brand').get_text(strip=True)
    try:
        sale_price = product_data_div.find(
            'p', class_='sale-price').get_text(strip=True)
    except AttributeError:
        sale_price = None

    try:
        price = product_data_div.find('p', class_='price').get_text(strip=True)
    except AttributeError:
        price = None

    product_info = {
        'Product Name': product_name,
        'Brand': brand,
        'Sale Price': sale_price,
        'Original Price Range': price
    }

    product_list.append(product_info)

df = pd.DataFrame(product_list)

df.to_csv('product_details.csv', index=False)

print("CSV file created successfully")
