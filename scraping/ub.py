# import requests
# from bs4 import BeautifulSoup

# # Send a GET request
# response = requests.get("https://ticketwala.pk/")

# # Check request status
# if response.status_code == 200:
#     html_content = response.text
#     soup = BeautifulSoup(html_content, features="html.parser")

#     main_point = soup.find('div', class_='grid grid-cols-1 md:grid-cols-2 gap-4')

#     print(main_point)
#     # Extract specific divs
#     # product_data_divs = soup.find_all('div', class_='custom-card')

#     # # If no data is found
#     # if not product_data_divs:
#     #     print("No data found! Check the class name or ensure the page isn't JavaScript-based.")
#     # else:
#     #     for product in product_data_divs:
#     #         print(product.text.strip())  # Print content inside each div
# else:
#     print(f"Request failed with status code: {response.status_code}")


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup

# # Set up headless mode
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode
# chrome_options.add_argument("--disable-gpu")  # Disable GPU for compatibility
# chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

# # Set up the WebDriver
# service = Service("C:\\Users\\feste\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")  # Replace with your ChromeDriver path
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Navigate to the target URL
# url = "https://ticketwala.pk/"
# driver.get(url)

# # Wait for dynamic content to load (optional, adjust as needed)
# driver.implicitly_wait(10)

# # Get the rendered HTML
# html = driver.page_source

# soup = BeautifulSoup(html, features="html.parser")

# main_point = soup.find('div', class_='grid grid-cols-1 md:grid-cols-2 gap-4')
# print(main_point)

# # Print the HTML or parse it using BeautifulSoup

# # event_divs = main_point.find_all('div', class_='custom-card')

# # print(event_divs)


# # Quit the browser
# driver.quit()


import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set up headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU for compatibility
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

# Set up the WebDriver
service = Service("C:\\Users\\feste\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")  # Replace with your ChromeDriver path
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the target URL
url = "https://ticketwala.pk/"
driver.get(url)

# Wait for dynamic content to load (optional, adjust as needed)
driver.implicitly_wait(10)

# Get the rendered HTML
html = driver.page_source

# Use BeautifulSoup to parse the page
soup = BeautifulSoup(html, features="html.parser")

# Find the main section containing the event listings
main_point = soup.find('div', class_='grid grid-cols-1 md:grid-cols-2 gap-4')

# Find all event divs
event_divs = main_point.find_all('a')

# Prepare data for CSV
events_data = []

# Loop through each event and extract the necessary information
for event in event_divs:
    title = event.find('h4').get_text(strip=True)
    date = event.find('span', class_='mr-3').get_text(strip=True)
    location = event.find_all('span')[-1].get_text(strip=True)
    image_url = event.find('img')['src']
    event_url = "https://ticketwala.pk" + event['href']
    
    events_data.append([title, date, location, image_url, event_url])

# Define CSV file path
csv_file = 'events.csv'

# Write data to CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Event Title", "Date", "Location", "Image URL", "Event URL"])  # Write header
    writer.writerows(events_data)  # Write event data

# Close the driver
driver.quit()

print(f"CSV file saved as {csv_file}")
