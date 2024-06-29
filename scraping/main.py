import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import os

product_urls = [
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
    "https://www.rugs-direct.com/Details/AmerRugs-Eternal-ETE22/136135",
    "https://www.rugs-direct.com/Details/AmerRugs-Berlin-Suney/145263",
    "https://www.rugs-direct.com/Details/AmerRugs-Vista-Raton/145287/233439",
    "https://www.rugs-direct.com/Details/AmerRugs-Berlin-Oxbow/145261",
    "https://www.rugs-direct.com/Details/AmerRugs-Vista-Duncan/145286/233437",
    "https://www.rugs-direct.com/Details/AmerRugs-Century-CEN18/139163",
    "https://www.rugs-direct.com/Details/AmerRugs-Arizona-Cameron/113192/201523",
    "https://www.rugs-direct.com/Details/AmerRugs-Raffia-Rafaele/125300/218759",
    "https://www.rugs-direct.com/Details/AmerRugs-Fairmont-Fiorella/139166",
    "https://www.rugs-direct.com/Details/AmerRugs-Fairmont-FAI2/139167",
    "https://www.rugs-direct.com/Details/AmerRugs-Alexandria-Aleme/136033",
    "https://www.rugs-direct.com/Details/AmerRugs-Maryland-Cecil/150081/241161",
    "https://www.rugs-direct.com/Details/AmerRugs-Cambridge-Cambria/132642",
    "https://www.rugs-direct.com/Details/AmerRugs-Abstract-Hammond/142573/229521",
    "https://www.rugs-direct.com/Details/AmerRugs-Arizona-Cameron/113192/180838",
    "https://www.rugs-direct.com/Details/AmerRugs-Arizona-Cameron/113192/180842",
    "https://www.rugs-direct.com/Details/AmerRugs-Alexandria-Alegria/133554",
    "https://www.rugs-direct.com/Details/AmerRugs-Alexandria-Aleeza/136035",
    "https://www.rugs-direct.com/Details/AmerRugs-Quartz-Desoto/150083/241170",
    "https://www.rugs-direct.com/Details/AmerRugs-Alexandria-Aleda/136034",
    "https://www.rugs-direct.com/Details/AmerRugs-Boscage-Ilford/142539/229439",
    "https://www.rugs-direct.com/Details/AmerRugs-Quartz-Desoto/150083/241169",
    "https://www.rugs-direct.com/Details/AmerRugs-Bohemian-Maldova/142577/229531",
    "https://www.rugs-direct.com/Details/AmerRugs-Quartz-Desoto/150083/241171",
    "https://www.rugs-direct.com/Details/AmerRugs-Alexandria-Aletha/133549/232534",
    "https://www.rugs-direct.com/Details/AmerRugs-Artifacts-Aralia/139159/232536",
    "https://www.rugs-direct.com/Details/AmerRugs-Hermitage-Dessavie/150078",
    "https://www.rugs-direct.com/Details/AmerRugs-Alexandria-Aleesha/133553",
    "https://www.rugs-direct.com/Details/AmerRugs-Hamilton-HAM02/136140",
    "https://www.rugs-direct.com/Details/AmerRugs-Bohemian-Malta/142578/229533",
    "https://www.rugs-direct.com/Details/AmerRugs-Artifacts-Aralia/139159/223417",
    "https://www.rugs-direct.com/Details/AmerRugs-Hamilton-HAM06/136144",
    "https://www.rugs-direct.com/Details/AmerRugs-Quartz-Desoto/150083/241168",
    "https://www.rugs-direct.com/Details/AmerRugs-Hamilton-HAM03/136141",
    "https://www.rugs-direct.com/Details/AmerRugs-Cambridge-Camilla/132629/231012",
    "https://www.rugs-direct.com/Details/AmerRugs-Metro-Shag/132647/213099",
    "https://www.rugs-direct.com/Details/AmerRugs-Montana-Joanna/145331",
    "https://www.rugs-direct.com/Details/AmerRugs-Maryland-Abbel/150080/241157",
    "https://www.rugs-direct.com/Details/AmerRugs-Metro-Shag/132647/213100",
    "https://www.rugs-direct.com/Details/AmerRugs-Artifacts-Arana/139157",
    "https://www.rugs-direct.com/Details/AmerRugs-Quartz-Desoto/150083/241167",
    "https://www.rugs-direct.com/Details/AmerRugs-Bohemian-Belarus/142575/229528",
    "https://www.rugs-direct.com/Details/AmerRugs-Boscage-BOS35/136108",
    "https://www.rugs-direct.com/Details/AmerRugs-Boscage-BOS33/136106",
    "https://www.rugs-direct.com/Details/AmerRugs-Manhattan-MAN35/133584",
    "https://www.rugs-direct.com/Details/AmerRugs-Artifacts-Arleth/133556",
    "https://www.rugs-direct.com/Details/AmerRugs-Boho-BOH3/133560",
    "https://www.rugs-direct.com/Details/AmerRugs-Cambridge-Camden/132644",
    "https://www.rugs-direct.com/Details/AmerRugs-Artifacts-Arriette/133558",
    "https://www.rugs-direct.com/Details/AmerRugs-Vista-Duncan/145286/233436",
    "https://www.rugs-direct.com/Details/AmerRugs-Boscage-Rothwell/136105",
    "https://www.rugs-direct.com/Details/AmerRugs-Boscage-BOS34/136107",
    "https://www.rugs-direct.com/Details/AmerRugs-Boscage-BOS36/136109",
    "https://www.rugs-direct.com/Details/AmerRugs-Manhattan-MAN41/133587",
    "https://www.rugs-direct.com/Details/AmerRugs-Aspen-Emara/150072",
    "https://www.rugs-direct.com/Details/AmerRugs-Manhattan-MAN40/133586",
    "https://www.rugs-direct.com/Details/AmerRugs-Aspen-Arra/150068",
    "https://www.rugs-direct.com/Details/AmerRugs-Metro-Shag/132647/223438",
    "https://www.rugs-direct.com/Details/AmerRugs-Metro-Shag/132647/213102",
    "https://www.rugs-direct.com/Details/AmerRugs-Manhattan-MAN3/133580",
    "https://www.rugs-direct.com/Details/AmerRugs-Odyssey-Odyssey/136146/218741",
    "https://www.rugs-direct.com/Details/AmerRugs-Metro-Shag/132647/223439",
    "https://www.rugs-direct.com/Details/AmerRugs-Hamilton-HAM07/136145",
    "https://www.rugs-direct.com/Details/AmerRugs-Cambridge-CAM60/136112",
    "https://www.rugs-direct.com/Details/AmerRugs-Bohemian-Curacao/142576/229530",
    "https://www.rugs-direct.com/Details/AmerRugs-Bohemian-Curacao/142576/229529",
    "https://www.rugs-direct.com/Details/AmerRugs-Odyssey-Odyssey/136146/218740",
    "https://www.rugs-direct.com/Details/AmerRugs-Cambridge-Cameron/132631",
    "https://www.rugs-direct.com/Details/AmerRugs-Aspen-Denise/150071",
    "https://www.rugs-direct.com/Details/AmerRugs-Aspen-Clara/150070/241142",
    "https://www.rugs-direct.com/Details/AmerRugs-Odyssey-Odyssey/136146/218744",
    "https://www.rugs-direct.com/Details/AmerRugs-Aspen-Clara/150070/241141",
    "https://www.rugs-direct.com/Details/AmerRugs-Aspen-Belen/150069",
    "https://www.rugs-direct.com/Details/AmerRugs-Manhattan-MAN42/133588",
    "https://www.rugs-direct.com/Details/AmerRugs-Odyssey-Odyssey/136146/218743"
]


def scrap(url, product_variant_divs_count):
    print(product_variant_divs_count)
    # Define the CSV file name
    csv_file = 'product_details.csv'

    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        try:
            existing_df = pd.read_csv(csv_file)
        except pd.errors.EmptyDataError:
            print(f"{csv_file} is empty. Creating a new DataFrame.")
            existing_df = pd.DataFrame()
    else:
        print(f"{csv_file} does not exist or is empty. Creating a new DataFrame.")
        existing_df = pd.DataFrame()

    # Patterns for extracting data
    pattern = re.compile(
        r'(\d+% Off)\$(\d{1,3}(?:,\d{3})*\.\d{2})\$(\d{1,3}(?:,\d{3})*\.\d{2})')
    color_pattern = re.compile(r'Color:\s*(.*)')
    size_pattern = re.compile(r'Size:\s*(.*)')
    price_pattern = re.compile(r'\$')

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

    if (len(image_urls) <= 1):
        variant_image = image_urls[0]
    else:
        variant_image = image_urls[1]

    # # Extracting variant information

    if product_variant_divs_count == 0:
        count = 0
        if count < len(image_urls):
            url = image_urls[count]
            count += 1
        try:
            product_size = product_data_divs.find_all(
                'p', class_='size-color-info')
            size_text = product_size[1].get_text(strip=True)
            match = size_pattern.search(size_text)
            size = match.group(1) if match else None
        except AttributeError:
            size = None
        try:
            product_original_price_div = product_data_divs.find(
                'div', class_='price-range text-red').get_text(strip=True)
            product_original_price = price_pattern.sub(
                '', product_original_price_div)
            product_sale_price_div = product_data_divs.find(
                'span', class_='msrp').get_text(strip=True)
            product_sale_price = price_pattern.sub(
                '', product_sale_price_div)

        except AttributeError:
            product_sale_price = product_original_price = None

        product_info = {
            'Title': product_name,
            'Body (HTML)': product_description,
            'Vendor': product_vendor,
            'Option1 Name': 'Color',
            'Option1 Value': color,
            'Option2 Name': "Size",
            'Option2 Value': size,
            'Variant Compare At Price': product_sale_price,
            'Variant Price': product_original_price,
            'Image Src': url,
            'Variant Image': variant_image,
            'Variant Inventory Qty': 1,
        }
        product_info.update(features_dict)

        # Converting the product info dictionary to a DataFrame
        new_df = pd.DataFrame([product_info])

        # Append the new data to the existing DataFrame
        existing_df = pd.concat([existing_df, new_df], ignore_index=True)

        while count != len(image_urls):
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

    else:

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

            while count != len(image_urls):
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
                existing_df = pd.concat(
                    [existing_df, new_df], ignore_index=True)

    # Save the updated DataFrame back to the CSV file
    existing_df.to_csv(csv_file, index=False)

    print(existing_df)
    print("CSV file added successfully")


for index, product_url in enumerate(product_urls):

    try:
        print(f"Fetching details for URL {
              index+1}/{len(product_urls)}: {product_url}")

        response = requests.get(product_url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch URL: {product_url} with error: {e}")
        continue

    if response.status_code != 200:
        print(f"Failed to fetch URL: {
              product_url} with status code: {response.status_code}")
        continue

    html_content = response.text
    soup = BeautifulSoup(html_content, features="html.parser")

    product_data_divs = soup.find('div', class_='right-panel')
    product_variant_divs = soup.find_all('div', class_='p-tile')
    product_variant_divs_count = (len(product_variant_divs))

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
        scrap(product_url, product_variant_divs_count)
    else:
        for i in range(len(href_list)):
            scrap(href_list[i], product_variant_divs_count)
