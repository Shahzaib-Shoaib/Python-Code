import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Prepare data for CSV
events_data = []

# Define a function to extract event data
def extract_event_data():
    # Get the rendered HTML after content loads
    html = driver.page_source
    soup = BeautifulSoup(html, features="html.parser")
    
    # Find the main section containing the event listings
    main_point = soup.find('div', class_='grid grid-cols-1 md:grid-cols-2 gap-4')

    # Find all event divs
    event_divs = main_point.find_all('a')

    # Loop through each event and extract the necessary information
    for event in event_divs:
        title = event.find('h4').get_text(strip=True)
        date = event.find('span', class_='mr-3').get_text(strip=True)
        location = event.find_all('span')[-1].get_text(strip=True)
        image_url = event.find('img')['src']
        event_url = "https://ticketwala.pk" + event['href']
        
        events_data.append([title, date, location, image_url, event_url])

# Extract initial events
extract_event_data()

# Counter to track the number of times "Load More" is clicked
load_more_clicks = 0

# Loop to click "Load More" button and extract more events
while load_more_clicks < 2:  # Limit to 2 clicks
    try:
        # Wait for the "Load More" button to be clickable using its unique class
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "bg-green") and contains(text(), "Load More")]'))
        )
        
        # Click the "Load More" button
        load_more_button.click()

        # Wait for the new events to load
        time.sleep(3)  # Adjust time if needed
        
        # Extract new events
        extract_event_data()

        # Increment the click counter
        load_more_clicks += 1

    except Exception as e:
        print("No more events or error:", e)
        break  # Exit the loop if no more events can be loaded

# Define CSV file path
csv_file = 'events_t.csv'

# Write data to CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Event Title", "Date", "Location", "Image URL", "Event URL"])  # Write header
    writer.writerows(events_data)  # Write event data

# Close the driver
driver.quit()

print(f"CSV file saved as {csv_file}")
