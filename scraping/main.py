import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import os


product_urls = [
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Zefira-Amena/143433/230809",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Kairos-Mirta/142430",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Cardamom-Idina/143395",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Lumal-Orame/150924",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Zefira-Amena/143433/230810",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Cardamom-Zascha/148827",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Zefira-Bellona/143434",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Cardamom-Ahava/143391/230736",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Zefira-Kyda/143437",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Cardamom-Dahir/148826",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-GarciaWashables-Lucinda/148774",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Nambe-Adrar/148852",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-VindagePrinted-Hepburn/146942",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Mahaba-Arpino/146200/234758",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Kairos-Adalee/142424",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Kairos-Chilton/142426",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Swoon-Lisana/146246",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Ferris-Orion/143702",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-CanteenaPrinted-Reeves/147583",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Swoon-Azura/144275/234813",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Bequest-Manor/148821",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Nadine-Taos/146416",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Nambe-Sahel/148855",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Jaida-Kohar/149129",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Cardamom-Sarang/147584",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Emrys-Beya/145231",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-CanteenaPrinted-Clanton/147580",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Mahaba-Lloria/146203/234761",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Mazarro-Viviana/148784/239136",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-CanteenaPrinted-Arkansas/147579",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Terra-Harkin/144286/231970",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Nadine-Mateo/146414",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Jolie-Lisette/145056/233086",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Terra-Harkin/144286/231971",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Jolie-Lisette/145056/233085",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Mahaba-Maji/144244/231909",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Zefira-Romano/148871/239284",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Nambe-Amanar/148853",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-CanteenaPrinted-Jesse/147581",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-IbisPrinted-Cosme/148840",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Jaida-Nicia/149130",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-IbisPrinted-Cantania/148839",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-VindagePrinted-Chaplin/146939",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-GarciaWashables-Sancho/148777",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Terra-Canna/144285",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-TorrenPillow-Lindy/145104/233157",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Mahaba-Hazina/144243",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Ferris-Natrix/149122",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Bahia-Sazon/145041",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Continuum-Cardinal/148829",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Jaida-Fantana/147598",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Terra-Katalia/144287/231973",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Swoon-Julia/146245",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Mahaba-Arpino/146200/234757",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Nadine-Yucca/146417",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Zefira-Althea/148870/239282",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Abrielle-Mariette/144208/231861",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-TorrenPillow-Lindy/145104/233159",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Sinclaire-Ilias/142433",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Swoon-Olivine/148862",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Leila-Camille/147613",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Abrielle-Feyre/144205/231857",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Bavell-Almeda/150903/242562",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Bavell-Norfolk/150904",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-EnBlanc-Sovis/146183",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Vanadey-Vesna/142452",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Jaida-Khoda/147599",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Kysa-Javyn/149133",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Nambe-Kidal/148854/239253",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Myriad-Emeline/143240",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Myriad-Jolene/143243",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Melo-Roane/145077",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Jaida-Dawson/147597",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Ferris-Gowon/149121",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-PampasPillow-Papyrus/144527/232376",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-PampasPillow-Papyrus/144527/232380",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-TorrenPillow-Lindy/145104/233156",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Abrielle-Devlin/144202/231851",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Audun-Tarian/144217",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Emrys-Annistyn/145229",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Ferris-Sobia/147122",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Tahiti-Iti/143981",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Continuum-Axiom/148828",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Audun-Jonet/144214/231867",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-LiriPillow-Iker/145069/233113",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-LiriPillow-HaskellLumbar/145068/233110",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Jaida-Treble/147601",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Mazarro-Sergio/148783/239135",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-ParablePillow-Imena/145093/233144",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Ferris-Yushan/147123",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Ferris-Gatlin/143408",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Jaida-Sachi/147600",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Jaida-Cree/147596",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Kysa-Odion/149135/239725",
    "https://www.rugs-direct.com/Details/VibebyJaipurLiving-Abrielle-Devlin/144202/231852",

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
