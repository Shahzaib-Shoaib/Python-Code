# import requests
# import re
# from bs4 import BeautifulSoup
# import pandas as pd
# url = 'https://www.rugs-direct.com/Details/AmerRugs-Legacy-Barton/145273'
# response = requests.get(url)
# html_content = response.text
# soup = BeautifulSoup(html_content, features="html.parser")
# color_pattern = re.compile(r'Color:\s*(.*)')

# product_data_divs = soup.find('div', class_='right-panel')
# product_list = []

# product_name = product_data_divs.find(
#     'h1', class_='pdp-title').get_text(strip=True)
# product_vendor = product_data_divs.find(
#     'a', class_='rd-primary-link').get_text(strip=True)
# product_color = product_data_divs.find(
#     'p', class_='size-color-info mb-p5').get_text()
# match = color_pattern.search(product_color)
# if match:
#     color = match.group(1)

# product_info = {
#     'Product Name': product_name,
#     'Vendor': product_vendor,
#     'Color': color

# }

# product_list.append(product_info)


# df = pd.DataFrame(product_list)

# print(df)
# df.to_csv("product-details")
