import requests
from bs4 import BeautifulSoup

# Send a GET request
response = requests.get("https://ticketwala.pk/")

# Check request status
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, features="html.parser")
    
    # Extract specific divs
    product_data_divs = soup.find_all('div', class_='custom-card')
    
    # If no data is found
    if not product_data_divs:
        print("No data found! Check the class name or ensure the page isn't JavaScript-based.")
    else:
        for product in product_data_divs:
            print(product.text.strip())  # Print content inside each div
else:
    print(f"Request failed with status code: {response.status_code}")
